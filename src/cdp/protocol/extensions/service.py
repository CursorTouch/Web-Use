"""CDP Extensions Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import ExtensionsMethods
from .events.service import ExtensionsEvents

if TYPE_CHECKING:
    from ...service import Client

class Extensions(ExtensionsMethods, ExtensionsEvents):
    """
    Defines commands and events for browser extensions.
    """
    def __init__(self, client: Client):
        """
        Initialize the Extensions domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        ExtensionsMethods.__init__(self, client)
        ExtensionsEvents.__init__(self, client)