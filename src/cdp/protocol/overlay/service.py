"""CDP Overlay Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import OverlayMethods
from .events.service import OverlayEvents

if TYPE_CHECKING:
    from ...service import Client

class Overlay(OverlayMethods, OverlayEvents):
    """
    This domain provides various functionality related to drawing atop the inspected page.
    """
    def __init__(self, client: Client):
        """
        Initialize the Overlay domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        OverlayMethods.__init__(self, client)
        OverlayEvents.__init__(self, client)