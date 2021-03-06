from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ._base import TelegramObject

if TYPE_CHECKING:  # pragma: no cover
    from .photo_size import PhotoSize


class Document(TelegramObject):
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    Source: https://core.telegram.org/bots/api#document
    """

    file_id: str
    """Identifier for this file, which can be used to download or reuse the file"""
    file_unique_id: str
    """Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file."""
    thumb: Optional[PhotoSize] = None
    """Document thumbnail as defined by sender"""
    file_name: Optional[str] = None
    """Original filename as defined by sender"""
    mime_type: Optional[str] = None
    """MIME type of the file as defined by sender"""
    file_size: Optional[int] = None
    """File size"""
