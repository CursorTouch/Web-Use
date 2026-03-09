"""CDP DeviceOrientation Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DeviceOrientationMethods:
    """
    Methods for the DeviceOrientation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DeviceOrientation methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def clear_device_orientation_override(self, params: clearDeviceOrientationOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears the overridden Device Orientation.    
        Args:
            params (clearDeviceOrientationOverrideParameters, optional): Parameters for the clearDeviceOrientationOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearDeviceOrientationOverride call.
        """
        return await self.client.send(method="DeviceOrientation.clearDeviceOrientationOverride", params=params, session_id=session_id)
    async def set_device_orientation_override(self, params: setDeviceOrientationOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides the Device Orientation.    
        Args:
            params (setDeviceOrientationOverrideParameters, optional): Parameters for the setDeviceOrientationOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDeviceOrientationOverride call.
        """
        return await self.client.send(method="DeviceOrientation.setDeviceOrientationOverride", params=params, session_id=session_id)