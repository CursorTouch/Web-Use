"""CDP Target Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class TargetMethods:
    """
    Methods for the Target domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Target methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def activate_target(self, params: activateTargetParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Activates (focuses) the target.    
        Args:
            params (activateTargetParameters, optional): Parameters for the activateTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the activateTarget call.
        """
        return await self.client.send(method="Target.activateTarget", params=params, session_id=session_id)
    async def attach_to_target(self, params: attachToTargetParameters | None = None, session_id: str | None = None) -> attachToTargetReturns:
        """
    Attaches to the target with given id.    
        Args:
            params (attachToTargetParameters, optional): Parameters for the attachToTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    attachToTargetReturns: The result of the attachToTarget call.
        """
        return await self.client.send(method="Target.attachToTarget", params=params, session_id=session_id)
    async def attach_to_browser_target(self, params: attachToBrowserTargetParameters | None = None, session_id: str | None = None) -> attachToBrowserTargetReturns:
        """
    Attaches to the browser target, only uses flat sessionId mode.    
        Args:
            params (attachToBrowserTargetParameters, optional): Parameters for the attachToBrowserTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    attachToBrowserTargetReturns: The result of the attachToBrowserTarget call.
        """
        return await self.client.send(method="Target.attachToBrowserTarget", params=params, session_id=session_id)
    async def close_target(self, params: closeTargetParameters | None = None, session_id: str | None = None) -> closeTargetReturns:
        """
    Closes the target. If the target is a page that gets closed too.    
        Args:
            params (closeTargetParameters, optional): Parameters for the closeTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    closeTargetReturns: The result of the closeTarget call.
        """
        return await self.client.send(method="Target.closeTarget", params=params, session_id=session_id)
    async def expose_dev_tools_protocol(self, params: exposeDevToolsProtocolParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Inject object to the target's main frame that provides a communication channel with browser target.  Injected object will be available as `window[bindingName]`.  The object has the following API: - `binding.send(json)` - a method to send messages over the remote debugging protocol - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.    
        Args:
            params (exposeDevToolsProtocolParameters, optional): Parameters for the exposeDevToolsProtocol method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the exposeDevToolsProtocol call.
        """
        return await self.client.send(method="Target.exposeDevToolsProtocol", params=params, session_id=session_id)
    async def create_browser_context(self, params: createBrowserContextParameters | None = None, session_id: str | None = None) -> createBrowserContextReturns:
        """
    Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one.    
        Args:
            params (createBrowserContextParameters, optional): Parameters for the createBrowserContext method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    createBrowserContextReturns: The result of the createBrowserContext call.
        """
        return await self.client.send(method="Target.createBrowserContext", params=params, session_id=session_id)
    async def get_browser_contexts(self, params: getBrowserContextsParameters | None = None, session_id: str | None = None) -> getBrowserContextsReturns:
        """
    Returns all browser contexts created with `Target.createBrowserContext` method.    
        Args:
            params (getBrowserContextsParameters, optional): Parameters for the getBrowserContexts method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getBrowserContextsReturns: The result of the getBrowserContexts call.
        """
        return await self.client.send(method="Target.getBrowserContexts", params=params, session_id=session_id)
    async def create_target(self, params: createTargetParameters | None = None, session_id: str | None = None) -> createTargetReturns:
        """
    Creates a new page.    
        Args:
            params (createTargetParameters, optional): Parameters for the createTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    createTargetReturns: The result of the createTarget call.
        """
        return await self.client.send(method="Target.createTarget", params=params, session_id=session_id)
    async def detach_from_target(self, params: detachFromTargetParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Detaches session with given id.    
        Args:
            params (detachFromTargetParameters, optional): Parameters for the detachFromTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the detachFromTarget call.
        """
        return await self.client.send(method="Target.detachFromTarget", params=params, session_id=session_id)
    async def dispose_browser_context(self, params: disposeBrowserContextParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes a BrowserContext. All the belonging pages will be closed without calling their beforeunload hooks.    
        Args:
            params (disposeBrowserContextParameters, optional): Parameters for the disposeBrowserContext method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disposeBrowserContext call.
        """
        return await self.client.send(method="Target.disposeBrowserContext", params=params, session_id=session_id)
    async def get_target_info(self, params: getTargetInfoParameters | None = None, session_id: str | None = None) -> getTargetInfoReturns:
        """
    Returns information about a target.    
        Args:
            params (getTargetInfoParameters, optional): Parameters for the getTargetInfo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getTargetInfoReturns: The result of the getTargetInfo call.
        """
        return await self.client.send(method="Target.getTargetInfo", params=params, session_id=session_id)
    async def get_targets(self, params: getTargetsParameters | None = None, session_id: str | None = None) -> getTargetsReturns:
        """
    Retrieves a list of available targets.    
        Args:
            params (getTargetsParameters, optional): Parameters for the getTargets method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getTargetsReturns: The result of the getTargets call.
        """
        return await self.client.send(method="Target.getTargets", params=params, session_id=session_id)
    async def set_auto_attach(self, params: setAutoAttachParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Controls whether to automatically attach to new targets which are considered to be directly related to this one (for example, iframes or workers). When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets. This also clears all targets added by `autoAttachRelated` from the list of targets to watch for creation of related targets. You might want to call this recursively for auto-attached targets to attach to all available targets.    
        Args:
            params (setAutoAttachParameters, optional): Parameters for the setAutoAttach method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAutoAttach call.
        """
        return await self.client.send(method="Target.setAutoAttach", params=params, session_id=session_id)
    async def auto_attach_related(self, params: autoAttachRelatedParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Adds the specified target to the list of targets that will be monitored for any related target creation (such as child frames, child workers and new versions of service worker) and reported through `attachedToTarget`. The specified target is also auto-attached. This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent `setAutoAttach`. Only available at the Browser target.    
        Args:
            params (autoAttachRelatedParameters, optional): Parameters for the autoAttachRelated method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the autoAttachRelated call.
        """
        return await self.client.send(method="Target.autoAttachRelated", params=params, session_id=session_id)
    async def set_discover_targets(self, params: setDiscoverTargetsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Controls whether to discover available targets and notify via `targetCreated/targetInfoChanged/targetDestroyed` events.    
        Args:
            params (setDiscoverTargetsParameters, optional): Parameters for the setDiscoverTargets method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDiscoverTargets call.
        """
        return await self.client.send(method="Target.setDiscoverTargets", params=params, session_id=session_id)
    async def set_remote_locations(self, params: setRemoteLocationsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables target discovery for the specified locations, when `setDiscoverTargets` was set to `true`.    
        Args:
            params (setRemoteLocationsParameters, optional): Parameters for the setRemoteLocations method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setRemoteLocations call.
        """
        return await self.client.send(method="Target.setRemoteLocations", params=params, session_id=session_id)
    async def get_dev_tools_target(self, params: getDevToolsTargetParameters | None = None, session_id: str | None = None) -> getDevToolsTargetReturns:
        """
    Gets the targetId of the DevTools page target opened for the given target (if any).    
        Args:
            params (getDevToolsTargetParameters, optional): Parameters for the getDevToolsTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getDevToolsTargetReturns: The result of the getDevToolsTarget call.
        """
        return await self.client.send(method="Target.getDevToolsTarget", params=params, session_id=session_id)
    async def open_dev_tools(self, params: openDevToolsParameters | None = None, session_id: str | None = None) -> openDevToolsReturns:
        """
    Opens a DevTools window for the target.    
        Args:
            params (openDevToolsParameters, optional): Parameters for the openDevTools method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    openDevToolsReturns: The result of the openDevTools call.
        """
        return await self.client.send(method="Target.openDevTools", params=params, session_id=session_id)