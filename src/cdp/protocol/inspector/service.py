"""CDP Inspector Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import InspectorMethods
from .events.service import InspectorEvents

if TYPE_CHECKING:
    from ...service import Client

class Inspector(InspectorMethods, InspectorEvents):
    """
    Access the Inspector domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Inspector domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        InspectorMethods.__init__(self, client)
        InspectorEvents.__init__(self, client)