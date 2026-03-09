"""CDP PWA Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import PWAMethods
from .events.service import PWAEvents

if TYPE_CHECKING:
    from ...service import Client

class PWA(PWAMethods, PWAEvents):
    """
    This domain allows interacting with the browser to control PWAs.
    """
    def __init__(self, client: Client):
        """
        Initialize the PWA domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        PWAMethods.__init__(self, client)
        PWAEvents.__init__(self, client)