"""CDP Target Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import TargetMethods
from .events.service import TargetEvents

if TYPE_CHECKING:
    from ...service import Client

class Target(TargetMethods, TargetEvents):
    """
    Supports additional targets discovery and allows to attach to them.
    """
    def __init__(self, client: Client):
        """
        Initialize the Target domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        TargetMethods.__init__(self, client)
        TargetEvents.__init__(self, client)