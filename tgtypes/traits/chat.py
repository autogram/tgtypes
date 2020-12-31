from typing import Any, List, Union

from pydantic.fields import FieldInfo
from pyrogram.types import User

from tgtypes.traits.base.named import NamedTrait
from tgtypes.traits.base.trait import TResult, Trait, UpdateTrait
from tgtypes.update import Update


class ChatIdTrait(NamedTrait):
    pass


# region experimentation

### PREBUILT ###


class ChatTitle(UpdateTrait):
    def filter(self, update: Update) -> bool:
        pass

    def extract(self, update: Update) -> TResult:
        pass


class ChatAdmins(UpdateTrait):
    pass


def Inject(key: Union[str, None]) -> Any:
    pass


### CUSTOM ###


def user_is_admin(
    admins: List[int] = Inject("MyBotAdmins"),
    user: User = Trait(User),
    chat_admins: List[User] = ChatAdmins(),
) -> bool:
    return True


@filter(user_is_admin)
async def do_something(

    chat_id: int = Trait(...), chat_title: str = ChatTitle(), html: HtmlBuilder = Inject()
):
    html.text(chat_id).raw(chat_title).bold(user_is_admin)


async def list_chat_members()

# endregion
