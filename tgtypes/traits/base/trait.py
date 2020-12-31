from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from tgtypes.models import Update

TResult = TypeVar("T", bound=type)


class Trait(Generic[TResult]):
    """
    Marks a type parameter as originating from any type of update, but returns the
    """

    def __init__(self, from_quoted: bool = False):
        self.from_quoted = from_quoted

    def __getattr__(self, item: TResult) -> TResult:
        self.expected_type = item
        return item


def Get(  # noqa: N802
    default: Any = None,
    *,
    alias: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    gt: Optional[float] = None,
    ge: Optional[float] = None,
    lt: Optional[float] = None,
    le: Optional[float] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    regex: Optional[str] = None,
    deprecated: Optional[bool] = None,
    **extra: Any,
) -> Any:
    return UpdateTrait(
        default=default,
        alias=alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        regex=regex,
        deprecated=deprecated,
        **extra,
    )


TResult = TypeVar("TResult")
TInput = TypeVar("TInput")


class ITraitExtractor(ABC, Generic[TInput, TResult]):
    @abstractmethod
    def filter(self, update: TInput) -> bool:
        ...

    @abstractmethod
    def extract(self, update: TInput) -> TResult:
        ...

    def cache_post_filter(self):
        ...

    def cache_post_extract(self):
        ...


class UpdateTrait(ITraitExtractor[Update, TResult], Generic[TResult]):
    """
    - TODO(idea): Hierarchies of dependencies
    - TODO: `AsyncTrait`s (with coroutines)
    """

    # client: IClient
    # context: TraitExtractionContext

    @abstractmethod
    def filter(self, update: Update) -> bool:
        ...

    @abstractmethod
    def extract(self, update: Update) -> TResult:
        ...

    # async def __call__(self, client: "pyrogram.Client", update: Update):
    #     raise NotImplementedError
    #
    # def __invert__(self):
    #     return InvertFilter(self)
    #
    # def __and__(self, other):
    #     return AndFilter(self, other)
    #
    # def __or__(self, other):
    #     return OrFilter(self, other)
