"""CDP HeadlessExperimental Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class HeadlessExperimentalMethods:
    """
    Methods for the HeadlessExperimental domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the HeadlessExperimental methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def begin_frame(self, params: beginFrameParameters | None = None, session_id: str | None = None) -> beginFrameReturns:
        """
    Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a screenshot from the resulting frame. Requires that the target was created with enabled BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also https://goo.gle/chrome-headless-rendering for more background.    
        Args:
            params (beginFrameParameters, optional): Parameters for the beginFrame method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    beginFrameReturns: The result of the beginFrame call.
        """
        return await self.client.send(method="HeadlessExperimental.beginFrame", params=params, session_id=session_id)