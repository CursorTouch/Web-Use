"""CDP Extensions Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class ExtensionsMethods:
    """
    Methods for the Extensions domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Extensions methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def trigger_action(self, params: triggerActionParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Runs an extension default action. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set.    
        Args:
            params (triggerActionParameters, optional): Parameters for the triggerAction method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the triggerAction call.
        """
        return await self.client.send(method="Extensions.triggerAction", params=params, session_id=session_id)
    async def load_unpacked(self, params: loadUnpackedParameters | None = None, session_id: str | None = None) -> loadUnpackedReturns:
        """
    Installs an unpacked extension from the filesystem similar to --load-extension CLI flags. Returns extension ID once the extension has been installed. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set.    
        Args:
            params (loadUnpackedParameters, optional): Parameters for the loadUnpacked method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    loadUnpackedReturns: The result of the loadUnpacked call.
        """
        return await self.client.send(method="Extensions.loadUnpacked", params=params, session_id=session_id)
    async def get_extensions(self, params: getExtensionsParameters | None = None, session_id: str | None = None) -> getExtensionsReturns:
        """
    Gets a list of all unpacked extensions. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set.    
        Args:
            params (getExtensionsParameters, optional): Parameters for the getExtensions method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getExtensionsReturns: The result of the getExtensions call.
        """
        return await self.client.send(method="Extensions.getExtensions", params=params, session_id=session_id)
    async def uninstall(self, params: uninstallParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Uninstalls an unpacked extension (others not supported) from the profile. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging.    
        Args:
            params (uninstallParameters, optional): Parameters for the uninstall method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the uninstall call.
        """
        return await self.client.send(method="Extensions.uninstall", params=params, session_id=session_id)
    async def get_storage_items(self, params: getStorageItemsParameters | None = None, session_id: str | None = None) -> getStorageItemsReturns:
        """
    Gets data from extension storage in the given `storageArea`. If `keys` is specified, these are used to filter the result.    
        Args:
            params (getStorageItemsParameters, optional): Parameters for the getStorageItems method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getStorageItemsReturns: The result of the getStorageItems call.
        """
        return await self.client.send(method="Extensions.getStorageItems", params=params, session_id=session_id)
    async def remove_storage_items(self, params: removeStorageItemsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes `keys` from extension storage in the given `storageArea`.    
        Args:
            params (removeStorageItemsParameters, optional): Parameters for the removeStorageItems method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeStorageItems call.
        """
        return await self.client.send(method="Extensions.removeStorageItems", params=params, session_id=session_id)
    async def clear_storage_items(self, params: clearStorageItemsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears extension storage in the given `storageArea`.    
        Args:
            params (clearStorageItemsParameters, optional): Parameters for the clearStorageItems method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearStorageItems call.
        """
        return await self.client.send(method="Extensions.clearStorageItems", params=params, session_id=session_id)
    async def set_storage_items(self, params: setStorageItemsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets `values` in extension storage in the given `storageArea`. The provided `values` will be merged with existing values in the storage area.    
        Args:
            params (setStorageItemsParameters, optional): Parameters for the setStorageItems method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setStorageItems call.
        """
        return await self.client.send(method="Extensions.setStorageItems", params=params, session_id=session_id)