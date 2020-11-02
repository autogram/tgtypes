import re
from typing import Any, Awaitable, Callable, Dict, TypeVar
from unittest.mock import Mock

import asynctest
import pytest
from pydantic import ValidationError

from tgtypes.descriptors.chat_descriptor import ChatDescriptor
from tgtypes.identities.chat_identity import ChatIdentity
from tgtypes.interfaces.chatresolver import IChatResolver

pytestmark = pytest.mark.asyncio


# region basic field tests

fields = {"chat_id": 123, "username": "@testing", "title_regex": ".*abc.*"}


def test_no_fields_set_raises_value_error():
    with pytest.raises(ValueError, match=r".*at least one.*"):
        ChatDescriptor()


def test_invalid_username_raises_validation_error():
    with pytest.raises(ValidationError, match=r"does not match regex"):
        ChatDescriptor(username="@kek tus")


def test_basic():
    c = ChatDescriptor(username="@henlo")
    assert c.username == "@henlo"


def test_any_field_set_no_error():
    for k, v in fields.items():
        kwargs = {k: v}
        c = ChatDescriptor(**kwargs)
        assert c.at_least_one(kwargs)
        assert getattr(c, k, None) == v


# endregion


# region lookup unit tests


T = TypeVar("T")


def wrap_async(func: Callable[..., T]) -> Callable[..., Awaitable[T]]:
    async def run(*args, **kwargs):
        return func(*args, **kwargs)

    return run


@pytest.mark.parametrize(
    "expected, descriptor_fields, method",
    [
        (Mock(ChatIdentity), {"username": "@any"}, "by_username"),
        (Mock(ChatIdentity), {"title_regex": re.compile(".*Henlo")}, "by_title_regex"),
        (Mock(ChatIdentity), {"chat_id": 12345}, "by_chat_id"),
        (None, {"username": "@any"}, "by_username"),
        (None, {"title_regex": re.compile(".*Henlo")}, "by_title_regex"),
        (None, {"chat_id": 12345}, "by_chat_id"),
    ],
)
async def test_resolve_by_x_happy_path(expected: Any, descriptor_fields: Dict, method: str):
    cd = ChatDescriptor(**descriptor_fields)

    resolver = asynctest.Mock(IChatResolver)
    mocked_resolve_call = getattr(resolver, f"resolve_chat_{method}")
    mocked_resolve_call.return_value = expected

    if expected is None:
        with pytest.raises(ValueError) as exc:
            await cd.resolve(resolver)
            exc.match(r"^Could not resolve chat identity of.*")
    else:
        res = await cd.resolve(resolver)
        assert res == expected

    mocked_resolve_call.assert_called_with(next(iter(descriptor_fields.values())))


# endregion
