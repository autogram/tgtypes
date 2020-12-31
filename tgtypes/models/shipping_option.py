from __future__ import annotations

from typing import TYPE_CHECKING, List

from ._base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    from .labeled_price import LabeledPrice


class ShippingOption(TelegramObject):
    """
    This object represents one shipping option.

    Source: https://core.telegram.org/bots/api#shippingoption
    """

    id: str
    """Shipping option identifier"""
    title: str
    """Option title"""
    prices: List[LabeledPrice]
    """List of price portions"""