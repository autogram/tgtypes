import asyncio
import inspect
from asyncio.events import AbstractEventLoop
from datetime import datetime, timedelta
from typing import Awaitable, Callable, Optional, TypeVar, Union, cast

from botkit.utils.sentinel import NotSet

T = TypeVar("T")


class DebouncedTask:
    def __init__(
        self,
        func: Callable[..., Union[T, Awaitable[T]]],
        delta: timedelta,
        num_runs: Optional[int] = 1,
        loop: AbstractEventLoop = None,
    ):
        if num_runs and num_runs <= 0:
            raise ValueError("Cannot run less than 1 time.")

        self.func = func
        self.delta = delta
        self.num_runs: Optional[int] = num_runs
        self.loop = loop or asyncio.get_event_loop()

        self._execution_count: int = 0
        self.last_result: Optional[T] = NotSet
        self._wait_future: Optional[asyncio.Future] = None
        self._deb_started_at: Optional[datetime] = None

    async def _run(self):
        while self.num_runs is None or self._execution_count < self.num_runs:
            while (remaining := self._calc_remaining_seconds()) > 0:
                await asyncio.sleep(remaining)

            await self.run_now()

    def _calc_remaining_seconds(self) -> float:
        return (datetime.utcnow() - (self._deb_started_at + self.delta)).total_seconds()

    async def run_now(self):
        result: Union[T, Awaitable[T]] = self.func()
        if inspect.isawaitable(result):
            result = cast(T, await result)

        self._execution_count += 1
        self.last_result = result

    def start(self):
        self.reset()
        self._wait_future = asyncio.ensure_future(self._run(), loop=self.loop)

    def reset(self):
        self._deb_started_at = datetime.utcnow()
