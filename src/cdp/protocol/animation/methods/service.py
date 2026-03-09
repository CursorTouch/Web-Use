"""CDP Animation Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AnimationMethods:
    """
    Methods for the Animation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Animation methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables animation domain notifications.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Animation.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables animation domain notifications.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Animation.enable", params=params, session_id=session_id)
    async def get_current_time(self, params: getCurrentTimeParameters | None = None, session_id: str | None = None) -> getCurrentTimeReturns:
        """
    Returns the current time of the an animation.    
        Args:
            params (getCurrentTimeParameters, optional): Parameters for the getCurrentTime method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCurrentTimeReturns: The result of the getCurrentTime call.
        """
        return await self.client.send(method="Animation.getCurrentTime", params=params, session_id=session_id)
    async def get_playback_rate(self, params: getPlaybackRateParameters | None = None, session_id: str | None = None) -> getPlaybackRateReturns:
        """
    Gets the playback rate of the document timeline.    
        Args:
            params (getPlaybackRateParameters, optional): Parameters for the getPlaybackRate method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getPlaybackRateReturns: The result of the getPlaybackRate call.
        """
        return await self.client.send(method="Animation.getPlaybackRate", params=params, session_id=session_id)
    async def release_animations(self, params: releaseAnimationsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Releases a set of animations to no longer be manipulated.    
        Args:
            params (releaseAnimationsParameters, optional): Parameters for the releaseAnimations method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the releaseAnimations call.
        """
        return await self.client.send(method="Animation.releaseAnimations", params=params, session_id=session_id)
    async def resolve_animation(self, params: resolveAnimationParameters | None = None, session_id: str | None = None) -> resolveAnimationReturns:
        """
    Gets the remote object of the Animation.    
        Args:
            params (resolveAnimationParameters, optional): Parameters for the resolveAnimation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    resolveAnimationReturns: The result of the resolveAnimation call.
        """
        return await self.client.send(method="Animation.resolveAnimation", params=params, session_id=session_id)
    async def seek_animations(self, params: seekAnimationsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Seek a set of animations to a particular time within each animation.    
        Args:
            params (seekAnimationsParameters, optional): Parameters for the seekAnimations method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the seekAnimations call.
        """
        return await self.client.send(method="Animation.seekAnimations", params=params, session_id=session_id)
    async def set_paused(self, params: setPausedParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets the paused state of a set of animations.    
        Args:
            params (setPausedParameters, optional): Parameters for the setPaused method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPaused call.
        """
        return await self.client.send(method="Animation.setPaused", params=params, session_id=session_id)
    async def set_playback_rate(self, params: setPlaybackRateParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets the playback rate of the document timeline.    
        Args:
            params (setPlaybackRateParameters, optional): Parameters for the setPlaybackRate method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPlaybackRate call.
        """
        return await self.client.send(method="Animation.setPlaybackRate", params=params, session_id=session_id)
    async def set_timing(self, params: setTimingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets the timing of an animation node.    
        Args:
            params (setTimingParameters, optional): Parameters for the setTiming method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setTiming call.
        """
        return await self.client.send(method="Animation.setTiming", params=params, session_id=session_id)