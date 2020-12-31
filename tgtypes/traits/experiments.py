from abc import ABC, abstractmethod
from typing import *

from pydantic.dataclasses import dataclass
from pyrogram import filters as f
from pyrogram.filters import Filter
from pyrogram.types import Message, User

from app.clients.telegram.botclients import BotClient
from app.clients.telegram.userclients import UserClient
from botkit.clients.client import IClient
from botkit.tghelpers.entities.message_entities import ParsedEntity, parse_entities


class TraitExtractionContext(dict):
    pass


class HashtagEntities(Trait[List[ParsedEntity]]):
    def extract(self, message):
        return parse_entities(message, "hashtag")

    def filter(self, message):
        return bool(self.extract(message))


class user(Filter, set):
    """Filter messages coming from one or more users.

    You can use `set bound methods <https://docs.python.org/3/library/stdtypes.html#set>`_ to manipulate the
    users container.

    Parameters:
        users (``int`` | ``str`` | ``list``):
            Pass one or more user ids/usernames to filter users.
            For you yourself, "me" or "self" can be used as well.
            Defaults to None (no users).
    """

    def __init__(self, users: int or str or list = None):
        users = [] if users is None else users if isinstance(users, list) else [users]

        super().__init__(
            "me" if u in ["me", "self"] else u.lower().strip("@") if isinstance(u, str) else u
            for u in users
        )

    async def __call__(self, _, message: Message):
        return message.from_user and (
            message.from_user.id in self
            or (message.from_user.username and message.from_user.username.lower() in self)
            or ("me" in self and message.from_user.is_self)
        )


class ChatAdmin(Trait[User]):
    def __init__(self, can_delete_messages: bool = True):
        pass

    def filter(self, message: Message) -> bool:
        pass

    def extract(self, message: Message) -> T:
        pass


class Sudoer(Trait[User]):
    def __init__(self, users: int or str or list = None):
        users = [] if users is None else users if isinstance(users, list) else [users]

        super().__init__(
            "me" if u in ["me", "self"] else u.lower().strip("@") if isinstance(u, str) else u
            for u in users
        )

    def filter(self, message: Message):
        pass

    def extract(self, message: Message) -> T:
        pass


class JosXa(Sudoer):
    pass


class RepliedToMessage(Trait[Message]):
    value: Message  # <-- this gets filled with the values

    def filter(self, message: Message) -> bool:
        return bool(self.extract(message))

    def extract(self, message: Message) -> Message:
        return message.reply_to_message


class RepliedToMessageId(Trait[Message]):
    value: Message  # <-- this gets filled with the values

    def filter(self, message: Message) -> bool:
        return bool(self.extract(message))

    def extract(self, message: Message) -> Message:
        return message.reply_to_message


@dataclass
class ParsedCommand:
    name: str
    args: List[str]
    args_str: str


class Command(Trait[ParsedCommand]):
    def __init__(
        self,
        commands: Union[str, Set[str]],
        prefixes: Union[str, Set[str]] = None,
        args: str = None,
    ):
        self.commands = commands
        self.prefixes = prefixes
        self.args_regex = args

    def filter(self, message: Message) -> bool:
        return f.command(self.commands, self.prefixes)(message)

    def extract(self, message: Message) -> ParsedCommand:
        return ParsedCommand(
            name=message.matches[0][0],
            args=message.matches[0][1:],
            args_str=" ".join(message.matches[0][1:]),
        )


class ChatId(Trait[int]):
    def filter(self, message: Message) -> bool:
        pass

    def extract(self, message: Message) -> T:
        pass


# region Throwaways


class TraitsHandler(object):
    pass


# endregion

# region Option 1 Demo


async def delete_last_n_messages(
    client: UserClient,
    cmd: ParsedCommand = Command("delete", {".", "/"}, args=r"([0-9]+)"),
    chat_id: int = ChatId(),
    _: User = ChatAdmin(can_delete_messages=True),
):
    num_to_delete = int(cmd.args_str)
    async for m in client.iter_history(chat_id, limit=num_to_delete, reverse=True):
        await m.delete()


# endregion

# region Option 2 Demo


@dataclass
class DeleteLastNMessagesContext:
    client: UserClient
    cmd: ParsedCommand = Command("delete", {".", "/"}, args=r"([0-9]+)")
    chat_id: int = ChatId()
    admin: User = ChatAdmin(can_delete_messages=True)


async def delete_last_n_messages_with_context(context: DeleteLastNMessagesContext):
    num_to_delete = int(context.cmd.args_str)
    async for m in context.client.iter_history(context.chat_id, limit=num_to_delete, reverse=True):
        await m.delete()


# endregion

# region Option 3 Demo


class DeleteLastNMessagesHandler(TraitsHandler):
    client: UserClient
    cmd: ParsedCommand = Command("delete", {".", "/"}, args=r"([0-9]+)")
    chat_id: int = ChatId()
    admin: User = ChatAdmin(can_delete_messages=True)

    async def invoke(self):
        num_to_delete = int(self.cmd.args_str)
        async for m in self.client.iter_history(self.chat_id, limit=num_to_delete, reverse=True):
            await m.delete()


# endregion

# region Option 1 Demo

# region
async def delete_last_n_messages(
    client: UserClient,
    cmd: Command("delete", {".", "/"}, args=r"([0-9]+)"),
    chat_id: ChatId(),
    user: ChatAdmin(can_delete_messages=True),
):
    num_to_delete = int(cmd.value.args_str)
    async for m in client.iter_history(chat_id.value, limit=num_to_delete, reverse=True):
        await m.delete()


# endregion
