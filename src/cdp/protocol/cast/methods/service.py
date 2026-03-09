"""CDP Cast Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class CastMethods:
    """
    Methods for the Cast domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Cast methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Starts observing for sinks that can be used for tab mirroring, and if set, sinks compatible with |presentationUrl| as well. When sinks are found, a |sinksUpdated| event is fired. Also starts observing for issue messages. When an issue is added or removed, an |issueUpdated| event is fired.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Cast.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Stops observing for sinks and issues.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Cast.disable", params=params, session_id=session_id)
    async def set_sink_to_use(self, params: setSinkToUseParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets a sink to be used when the web page requests the browser to choose a sink via Presentation API, Remote Playback API, or Cast SDK.    
        Args:
            params (setSinkToUseParameters, optional): Parameters for the setSinkToUse method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSinkToUse call.
        """
        return await self.client.send(method="Cast.setSinkToUse", params=params, session_id=session_id)
    async def start_desktop_mirroring(self, params: startDesktopMirroringParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Starts mirroring the desktop to the sink.    
        Args:
            params (startDesktopMirroringParameters, optional): Parameters for the startDesktopMirroring method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startDesktopMirroring call.
        """
        return await self.client.send(method="Cast.startDesktopMirroring", params=params, session_id=session_id)
    async def start_tab_mirroring(self, params: startTabMirroringParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Starts mirroring the tab to the sink.    
        Args:
            params (startTabMirroringParameters, optional): Parameters for the startTabMirroring method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startTabMirroring call.
        """
        return await self.client.send(method="Cast.startTabMirroring", params=params, session_id=session_id)
    async def stop_casting(self, params: stopCastingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Stops the active Cast session on the sink.    
        Args:
            params (stopCastingParameters, optional): Parameters for the stopCasting method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopCasting call.
        """
        return await self.client.send(method="Cast.stopCasting", params=params, session_id=session_id)