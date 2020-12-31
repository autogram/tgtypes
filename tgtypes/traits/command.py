from tgtypes.traits.message import MessageTextTrait


class CommandTrait(UpdateTrait):
    def __init__(
        self,
        text: str = Depends(MessageTextTrait(..., regex=r"\/.*")),
        entity: MessageEntity = CommandEntityTrait(),
    ):
        self.text = text
        self.entity = entity
