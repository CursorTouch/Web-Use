"""CDP DOMSnapshot Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DOMSnapshotMethods
from .events.service import DOMSnapshotEvents

if TYPE_CHECKING:
    from ...service import Client

class DOMSnapshot(DOMSnapshotMethods, DOMSnapshotEvents):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMSnapshot domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DOMSnapshotMethods.__init__(self, client)
        DOMSnapshotEvents.__init__(self, client)