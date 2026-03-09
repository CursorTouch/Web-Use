"""CDP WebAuthn Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import WebAuthnMethods
from .events.service import WebAuthnEvents

if TYPE_CHECKING:
    from ...service import Client

class WebAuthn(WebAuthnMethods, WebAuthnEvents):
    """
    This domain allows configuring virtual authenticators to test the WebAuthn API.
    """
    def __init__(self, client: Client):
        """
        Initialize the WebAuthn domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        WebAuthnMethods.__init__(self, client)
        WebAuthnEvents.__init__(self, client)