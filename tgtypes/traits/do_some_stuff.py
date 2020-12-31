import inspect
from pydantic.dataclasses import dataclass
import re
from typing import Type
from injector import Injector, Binder, NoInject
from typing import (
    Any,
    Callable,
    ClassVar,
    Generic,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    AbstractSet,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
    AsyncIterator,
    AsyncIterable,
    Coroutine,
    Collection,
    AsyncGenerator,
    Deque,
    Dict,
    List,
    Set,
    FrozenSet,
    NamedTuple,
    Generator,
    cast,
    overload,
    TYPE_CHECKING,
)

from pydantic import BaseModel
from typing_extensions import Annotated, TypedDict

from unittest.mock import Mock
from tgtypes.models import Update, Message

from tgtypes.traits.base.trait import Trait, UpdateTrait


def mock(t: Type, **configure):
    mock = Mock(t)
    mock.configure_mock(**configure)
    return mock


update = mock(Update, message=mock(Message, message_id=123,))


class WhatWeNeed(BaseModel):
    text: str
    quoted_message: Message
    reply_message: Message


class X:
    def __init__(self, arg):
        print("init")


def a(b=X(Message.text)):
    pass


a = []


class QuotedMessage:
    def __init__(self):
        pass


trait_marker = None

T = TypeVar("T")

TraitType = Annotated[T, trait_marker]

TT = TypeVar("TT")


class AttrPathSpec:
    def __init__(self, type_: Type):
        self.__type_ = type_


# noinspection PyPep8Naming
def Get(t: TT) -> AttrPathSpec:
    for name, val in t.__fields__.items():
        if name.startswith("_"):
            continue
        setattr(t, name, AttrPathSpec(t))
        print(name, val)

    return t


MyTrait[Message].text


class Me:
    id: TraitType[int]


def only():
    pass


class CommandArg:
    pass


class Foo(BaseModel):
    bar: str


class TMessage(Message):
    pass


def parse_simple_cmd(message_text: str = Get(Message).text):
    pass


print(inspect.signature(parse_simple_cmd))


class DeletionArgs:
    pass


def delete_last_n_in_chat():
    pass


# def test_extract_chat_and_user_ids():
#     def testing(chat_id: TraitType[int], user_id: TraitType[int], w: TraitType[WhatWeNeed]):
#         assert isinstance(chat_id, int)
#         assert isinstance(user_id, int)
#         assert w


def configure(binder: Binder):
    binder.bind(QuotedMessage)


if __name__ == "__main__":
    pass
