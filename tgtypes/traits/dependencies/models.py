from typing import Callable, List, Optional, Sequence

from pydantic.fields import ModelField


class Dependant:
    def __init__(
        self,
        *,
        message_traits: Optional[List[ModelField]] = None,
        callback_query_traits: Optional[List[ModelField]] = None,
        inline_query_traits: Optional[List[ModelField]] = None,
        poll_traits: Optional[List[ModelField]] = None,
        user_status_traits: Optional[List[ModelField]] = None,
        name: Optional[str] = None,
        call: Optional[Callable] = None,
    ) -> None:
        self.message_traits = message_traits
        self.callback_query_traits = callback_query_traits
        self.inline_query_traits = inline_query_traits
        self.poll_traits = poll_traits
        self.user_status_traits = user_status_traits
        self.name = name
        self.call = call
