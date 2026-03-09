"""CDP ServiceWorker Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class ServiceWorkerMethods:
    """
    Methods for the ServiceWorker domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the ServiceWorker methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def deliver_push_message(self, params: deliverPushMessageParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for deliverPushMessage.    
        Args:
            params (deliverPushMessageParameters, optional): Parameters for the deliverPushMessage method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deliverPushMessage call.
        """
        return await self.client.send(method="ServiceWorker.deliverPushMessage", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for disable.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="ServiceWorker.disable", params=params, session_id=session_id)
    async def dispatch_sync_event(self, params: dispatchSyncEventParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for dispatchSyncEvent.    
        Args:
            params (dispatchSyncEventParameters, optional): Parameters for the dispatchSyncEvent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the dispatchSyncEvent call.
        """
        return await self.client.send(method="ServiceWorker.dispatchSyncEvent", params=params, session_id=session_id)
    async def dispatch_periodic_sync_event(self, params: dispatchPeriodicSyncEventParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for dispatchPeriodicSyncEvent.    
        Args:
            params (dispatchPeriodicSyncEventParameters, optional): Parameters for the dispatchPeriodicSyncEvent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the dispatchPeriodicSyncEvent call.
        """
        return await self.client.send(method="ServiceWorker.dispatchPeriodicSyncEvent", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for enable.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="ServiceWorker.enable", params=params, session_id=session_id)
    async def set_force_update_on_page_load(self, params: setForceUpdateOnPageLoadParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setForceUpdateOnPageLoad.    
        Args:
            params (setForceUpdateOnPageLoadParameters, optional): Parameters for the setForceUpdateOnPageLoad method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setForceUpdateOnPageLoad call.
        """
        return await self.client.send(method="ServiceWorker.setForceUpdateOnPageLoad", params=params, session_id=session_id)
    async def skip_waiting(self, params: skipWaitingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for skipWaiting.    
        Args:
            params (skipWaitingParameters, optional): Parameters for the skipWaiting method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the skipWaiting call.
        """
        return await self.client.send(method="ServiceWorker.skipWaiting", params=params, session_id=session_id)
    async def start_worker(self, params: startWorkerParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for startWorker.    
        Args:
            params (startWorkerParameters, optional): Parameters for the startWorker method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startWorker call.
        """
        return await self.client.send(method="ServiceWorker.startWorker", params=params, session_id=session_id)
    async def stop_all_workers(self, params: stopAllWorkersParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for stopAllWorkers.    
        Args:
            params (stopAllWorkersParameters, optional): Parameters for the stopAllWorkers method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopAllWorkers call.
        """
        return await self.client.send(method="ServiceWorker.stopAllWorkers", params=params, session_id=session_id)
    async def stop_worker(self, params: stopWorkerParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for stopWorker.    
        Args:
            params (stopWorkerParameters, optional): Parameters for the stopWorker method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopWorker call.
        """
        return await self.client.send(method="ServiceWorker.stopWorker", params=params, session_id=session_id)
    async def unregister(self, params: unregisterParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for unregister.    
        Args:
            params (unregisterParameters, optional): Parameters for the unregister method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the unregister call.
        """
        return await self.client.send(method="ServiceWorker.unregister", params=params, session_id=session_id)
    async def update_registration(self, params: updateRegistrationParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for updateRegistration.    
        Args:
            params (updateRegistrationParameters, optional): Parameters for the updateRegistration method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the updateRegistration call.
        """
        return await self.client.send(method="ServiceWorker.updateRegistration", params=params, session_id=session_id)