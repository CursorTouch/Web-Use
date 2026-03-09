"""CDP HeapProfiler Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class HeapProfilerMethods:
    """
    Methods for the HeapProfiler domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the HeapProfiler methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def add_inspected_heap_object(self, params: addInspectedHeapObjectParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).    
        Args:
            params (addInspectedHeapObjectParameters, optional): Parameters for the addInspectedHeapObject method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the addInspectedHeapObject call.
        """
        return await self.client.send(method="HeapProfiler.addInspectedHeapObject", params=params, session_id=session_id)
    async def collect_garbage(self, params: collectGarbageParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for collectGarbage.    
        Args:
            params (collectGarbageParameters, optional): Parameters for the collectGarbage method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the collectGarbage call.
        """
        return await self.client.send(method="HeapProfiler.collectGarbage", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for disable.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="HeapProfiler.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for enable.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="HeapProfiler.enable", params=params, session_id=session_id)
    async def get_heap_object_id(self, params: getHeapObjectIdParameters | None = None, session_id: str | None = None) -> getHeapObjectIdReturns:
        """
    No description available for getHeapObjectId.    
        Args:
            params (getHeapObjectIdParameters, optional): Parameters for the getHeapObjectId method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getHeapObjectIdReturns: The result of the getHeapObjectId call.
        """
        return await self.client.send(method="HeapProfiler.getHeapObjectId", params=params, session_id=session_id)
    async def get_object_by_heap_object_id(self, params: getObjectByHeapObjectIdParameters | None = None, session_id: str | None = None) -> getObjectByHeapObjectIdReturns:
        """
    No description available for getObjectByHeapObjectId.    
        Args:
            params (getObjectByHeapObjectIdParameters, optional): Parameters for the getObjectByHeapObjectId method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getObjectByHeapObjectIdReturns: The result of the getObjectByHeapObjectId call.
        """
        return await self.client.send(method="HeapProfiler.getObjectByHeapObjectId", params=params, session_id=session_id)
    async def get_sampling_profile(self, params: getSamplingProfileParameters | None = None, session_id: str | None = None) -> getSamplingProfileReturns:
        """
    No description available for getSamplingProfile.    
        Args:
            params (getSamplingProfileParameters, optional): Parameters for the getSamplingProfile method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getSamplingProfileReturns: The result of the getSamplingProfile call.
        """
        return await self.client.send(method="HeapProfiler.getSamplingProfile", params=params, session_id=session_id)
    async def start_sampling(self, params: startSamplingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for startSampling.    
        Args:
            params (startSamplingParameters, optional): Parameters for the startSampling method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startSampling call.
        """
        return await self.client.send(method="HeapProfiler.startSampling", params=params, session_id=session_id)
    async def start_tracking_heap_objects(self, params: startTrackingHeapObjectsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for startTrackingHeapObjects.    
        Args:
            params (startTrackingHeapObjectsParameters, optional): Parameters for the startTrackingHeapObjects method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startTrackingHeapObjects call.
        """
        return await self.client.send(method="HeapProfiler.startTrackingHeapObjects", params=params, session_id=session_id)
    async def stop_sampling(self, params: stopSamplingParameters | None = None, session_id: str | None = None) -> stopSamplingReturns:
        """
    No description available for stopSampling.    
        Args:
            params (stopSamplingParameters, optional): Parameters for the stopSampling method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    stopSamplingReturns: The result of the stopSampling call.
        """
        return await self.client.send(method="HeapProfiler.stopSampling", params=params, session_id=session_id)
    async def stop_tracking_heap_objects(self, params: stopTrackingHeapObjectsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for stopTrackingHeapObjects.    
        Args:
            params (stopTrackingHeapObjectsParameters, optional): Parameters for the stopTrackingHeapObjects method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopTrackingHeapObjects call.
        """
        return await self.client.send(method="HeapProfiler.stopTrackingHeapObjects", params=params, session_id=session_id)
    async def take_heap_snapshot(self, params: takeHeapSnapshotParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for takeHeapSnapshot.    
        Args:
            params (takeHeapSnapshotParameters, optional): Parameters for the takeHeapSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the takeHeapSnapshot call.
        """
        return await self.client.send(method="HeapProfiler.takeHeapSnapshot", params=params, session_id=session_id)