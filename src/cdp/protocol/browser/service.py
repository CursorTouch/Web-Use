"""CDP Browser Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import BrowserMethods
from .events.service import BrowserEvents

if TYPE_CHECKING:
    from ...service import Client

class Browser(BrowserMethods, BrowserEvents):
    """
    The Browser domain defines methods and events for browser managing.
    """
    def __init__(self, client: Client):
        """
        Initialize the Browser domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        BrowserMethods.__init__(self, client)
        BrowserEvents.__init__(self, client)