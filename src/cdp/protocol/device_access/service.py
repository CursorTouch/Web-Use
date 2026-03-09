"""CDP DeviceAccess Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DeviceAccessMethods
from .events.service import DeviceAccessEvents

if TYPE_CHECKING:
    from ...service import Client

class DeviceAccess(DeviceAccessMethods, DeviceAccessEvents):
    """
    Access the DeviceAccess domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DeviceAccess domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DeviceAccessMethods.__init__(self, client)
        DeviceAccessEvents.__init__(self, client)