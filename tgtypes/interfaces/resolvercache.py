import sys
from abc import ABC, abstractmethod
from typing import (
    Any,
    Coroutine,
    Dict,
    TypeVar,
)

T = TypeVar("T")


class IResolverCache(Dict, ABC):
    @abstractmethod
    async def dump_data(self) -> None:
        ...

    @abstractmethod
    async def ensure_initialized(self) -> None:
        ...

    @abstractmethod
    async def setdefault_lazy(self, key: Any, coro: Coroutine[Any, Any, T]) -> T:
        ...


if "haps" in sys.modules:
    import traceback

    try:
        import haps

        haps.base(IResolverCache)
    except:
        traceback.print_exc()
