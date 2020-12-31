from typing import *

T = TypeVar("T")


class AsyncLazyDict(Dict):
    async def setdefault_lazy(self, key: Any, coro: Coroutine[Any, Any, T]) -> T:
        """
        Acts like `setdefault` in dictionaries, but instead of accepting the value it takes a coroutine that
        will be executed if the key is not yet set.

        Args:
            key: The key to look up
            coro: The coroutine to execute when the key is not available.

        Returns:
            The existing or awaited value of the coroutine

        """
        if self.get(key):
            return key
        self[key] = (val := await coro)
        return val
