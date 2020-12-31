- Merge with aiogram's v3 models: https://github.com/aiogram/aiogram/blob/dev-3.x/aiogram/api/types/base.py


## Ideas for Traits

```python
@out(gender=Memory[User])
def gender(
    display_name: str = Get(DisplayName(User)), gender: str = Get(Memory[User]),
) -> StateTransition[int]:
    logger.info(
    "Gender of {User}: {Gender}", display_name, gender
    )
    update.message.reply_text(
    "I see! Please send me a photo of yourself, "
    "so I know what you look like, or send /skip if you don't want to.", reply_markup=ReplyKeyboardRemove(),
    )

    return PHOTO  # type: int
```
