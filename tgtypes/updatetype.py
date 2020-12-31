from enum import Enum, auto

from boltons.typeutils import classproperty


class UpdateType(Enum):
    raw = "Raw"
    message = "Message"
    channel_post = "ChannelPost"
    edited_message = "EditedMessage"
    deleted_messages = "DeletedMessages"
    callback_query = "CallbackQuery"
    inline_query = "InlineQuery"
    poll = "Poll"
    user_status = "UserStatus"
    chosen_inline_result = "ChosenInlineResult"
    start_command = "StartCommand"

    # noinspection PyMethodParameters
    @classproperty
    def all(cls):
        return [
            cls.raw,
            cls.message,
            cls.channel_post,
            cls.edited_message,
            cls.deleted_messages,
            cls.callback_query,
            cls.inline_query,
            cls.poll,
            cls.user_status,
            cls.chosen_inline_result,
            cls.start_command,
        ]
