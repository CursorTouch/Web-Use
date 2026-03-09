"""CDP SystemInfo Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import SystemInfoMethods
from .events.service import SystemInfoEvents

if TYPE_CHECKING:
    from ...service import Client

class SystemInfo(SystemInfoMethods, SystemInfoEvents):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """
    def __init__(self, client: Client):
        """
        Initialize the SystemInfo domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        SystemInfoMethods.__init__(self, client)
        SystemInfoEvents.__init__(self, client)