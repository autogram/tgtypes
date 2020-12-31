from __future__ import annotations

from typing import TYPE_CHECKING

from ._base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class GameHighScore(TelegramObject):
    """
    This object represents one row of the high scores table for a game.
    And that's about all we've got for now.
    If you've got any questions, please check out our Bot FAQ

    Source: https://core.telegram.org/bots/api#gamehighscore
    """

    position: int
    """Position in high score table for the game"""
    user: User
    """User"""
    score: int
    """Score"""
