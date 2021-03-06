from __future__ import annotations

from typing import List, Optional

from ._base import TelegramObject


class WebhookInfo(TelegramObject):
    """
    Contains information about the current status of a webhook.

    Source: https://core.telegram.org/bots/api#webhookinfo
    """

    url: str
    """Webhook URL, may be empty if webhook is not set up"""
    has_custom_certificate: bool
    """True, if a custom certificate was provided for webhook certificate checks"""
    pending_update_count: int
    """Number of updates awaiting delivery"""
    last_error_date: Optional[int] = None
    """Unix time for the most recent error that happened when trying to deliver an update via
    webhook"""
    last_error_message: Optional[str] = None
    """Error message in human-readable format for the most recent error that happened when trying
    to deliver an update via webhook"""
    max_connections: Optional[int] = None
    """Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery"""
    allowed_updates: Optional[List[str]] = None
    """A list of update types the bot is subscribed to. Defaults to all update types"""
