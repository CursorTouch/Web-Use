"""CDP Page Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import PageMethods
from .events.service import PageEvents

if TYPE_CHECKING:
    from ...service import Client

class Page(PageMethods, PageEvents):
    """
    Actions and events related to the inspected page belong to the page domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Page domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        PageMethods.__init__(self, client)
        PageEvents.__init__(self, client)