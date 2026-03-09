"""CDP DeviceOrientation Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import DeviceOrientationMethods
from .events.service import DeviceOrientationEvents

if TYPE_CHECKING:
    from ...service import Client

class DeviceOrientation(DeviceOrientationMethods, DeviceOrientationEvents):
    """
    Access the DeviceOrientation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DeviceOrientation domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        DeviceOrientationMethods.__init__(self, client)
        DeviceOrientationEvents.__init__(self, client)