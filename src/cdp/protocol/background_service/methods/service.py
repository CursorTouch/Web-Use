"""CDP BackgroundService Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class BackgroundServiceMethods:
    """
    Methods for the BackgroundService domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the BackgroundService methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def start_observing(self, params: startObservingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables event updates for the service.    
        Args:
            params (startObservingParameters, optional): Parameters for the startObserving method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startObserving call.
        """
        return await self.client.send(method="BackgroundService.startObserving", params=params, session_id=session_id)
    async def stop_observing(self, params: stopObservingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables event updates for the service.    
        Args:
            params (stopObservingParameters, optional): Parameters for the stopObserving method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopObserving call.
        """
        return await self.client.send(method="BackgroundService.stopObserving", params=params, session_id=session_id)
    async def set_recording(self, params: setRecordingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set the recording state for the service.    
        Args:
            params (setRecordingParameters, optional): Parameters for the setRecording method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setRecording call.
        """
        return await self.client.send(method="BackgroundService.setRecording", params=params, session_id=session_id)
    async def clear_events(self, params: clearEventsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears all stored data for the service.    
        Args:
            params (clearEventsParameters, optional): Parameters for the clearEvents method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearEvents call.
        """
        return await self.client.send(method="BackgroundService.clearEvents", params=params, session_id=session_id)