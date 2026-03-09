"""CDP Tracing Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class TracingMethods:
    """
    Methods for the Tracing domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Tracing methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def end(self, params: endParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Stop trace events collection.    
        Args:
            params (endParameters, optional): Parameters for the end method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the end call.
        """
        return await self.client.send(method="Tracing.end", params=params, session_id=session_id)
    async def get_categories(self, params: getCategoriesParameters | None = None, session_id: str | None = None) -> getCategoriesReturns:
        """
    Gets supported tracing categories.    
        Args:
            params (getCategoriesParameters, optional): Parameters for the getCategories method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCategoriesReturns: The result of the getCategories call.
        """
        return await self.client.send(method="Tracing.getCategories", params=params, session_id=session_id)
    async def get_track_event_descriptor(self, params: getTrackEventDescriptorParameters | None = None, session_id: str | None = None) -> getTrackEventDescriptorReturns:
        """
    Return a descriptor for all available tracing categories.    
        Args:
            params (getTrackEventDescriptorParameters, optional): Parameters for the getTrackEventDescriptor method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getTrackEventDescriptorReturns: The result of the getTrackEventDescriptor call.
        """
        return await self.client.send(method="Tracing.getTrackEventDescriptor", params=params, session_id=session_id)
    async def record_clock_sync_marker(self, params: recordClockSyncMarkerParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Record a clock sync marker in the trace.    
        Args:
            params (recordClockSyncMarkerParameters, optional): Parameters for the recordClockSyncMarker method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the recordClockSyncMarker call.
        """
        return await self.client.send(method="Tracing.recordClockSyncMarker", params=params, session_id=session_id)
    async def request_memory_dump(self, params: requestMemoryDumpParameters | None = None, session_id: str | None = None) -> requestMemoryDumpReturns:
        """
    Request a global memory dump.    
        Args:
            params (requestMemoryDumpParameters, optional): Parameters for the requestMemoryDump method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestMemoryDumpReturns: The result of the requestMemoryDump call.
        """
        return await self.client.send(method="Tracing.requestMemoryDump", params=params, session_id=session_id)
    async def start(self, params: startParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Start trace events collection.    
        Args:
            params (startParameters, optional): Parameters for the start method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the start call.
        """
        return await self.client.send(method="Tracing.start", params=params, session_id=session_id)