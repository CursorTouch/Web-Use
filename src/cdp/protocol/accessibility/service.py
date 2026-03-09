"""CDP Accessibility Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import AccessibilityMethods
from .events.service import AccessibilityEvents

if TYPE_CHECKING:
    from ...service import Client

class Accessibility(AccessibilityMethods, AccessibilityEvents):
    """
    Access the Accessibility domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Accessibility domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        AccessibilityMethods.__init__(self, client)
        AccessibilityEvents.__init__(self, client)