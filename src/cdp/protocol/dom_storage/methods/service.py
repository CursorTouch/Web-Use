"""CDP DOMStorage Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DOMStorageMethods:
    """
    Methods for the DOMStorage domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOMStorage methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def clear(self, params: clearParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for clear.    
        Args:
            params (clearParameters, optional): Parameters for the clear method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clear call.
        """
        return await self.client.send(method="DOMStorage.clear", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables storage tracking, prevents storage events from being sent to the client.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="DOMStorage.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables storage tracking, storage events will now be delivered to the client.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="DOMStorage.enable", params=params, session_id=session_id)
    async def get_dom_storage_items(self, params: getDOMStorageItemsParameters | None = None, session_id: str | None = None) -> getDOMStorageItemsReturns:
        """
    No description available for getDOMStorageItems.    
        Args:
            params (getDOMStorageItemsParameters, optional): Parameters for the getDOMStorageItems method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getDOMStorageItemsReturns: The result of the getDOMStorageItems call.
        """
        return await self.client.send(method="DOMStorage.getDOMStorageItems", params=params, session_id=session_id)
    async def remove_dom_storage_item(self, params: removeDOMStorageItemParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for removeDOMStorageItem.    
        Args:
            params (removeDOMStorageItemParameters, optional): Parameters for the removeDOMStorageItem method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeDOMStorageItem call.
        """
        return await self.client.send(method="DOMStorage.removeDOMStorageItem", params=params, session_id=session_id)
    async def set_dom_storage_item(self, params: setDOMStorageItemParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setDOMStorageItem.    
        Args:
            params (setDOMStorageItemParameters, optional): Parameters for the setDOMStorageItem method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDOMStorageItem call.
        """
        return await self.client.send(method="DOMStorage.setDOMStorageItem", params=params, session_id=session_id)