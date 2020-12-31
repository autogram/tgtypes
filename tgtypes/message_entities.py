from typing_extensions import Literal

MessageEntityType = Literal[
    "mention",
    "hashtag",
    "cashtag",
    "bot_command",
    "url",
    "email",
    "bold",
    "italic",
    "code",
    "pre",
    "underline",
    "strike",
    "blockquote",
    "text_link",
    "text_mention",
    "phone_number",
]
