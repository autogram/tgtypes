from typing import Literal, Protocol, runtime_checkable, Optional


@runtime_checkable
class Chat(Protocol):
    id: int
    type: Literal["private", "bot", "group", "supergroup", "channel"]
    title: Optional[str]
