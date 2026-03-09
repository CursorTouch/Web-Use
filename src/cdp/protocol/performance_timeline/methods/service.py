"""CDP PerformanceTimeline Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PerformanceTimelineMethods:
    """
    Methods for the PerformanceTimeline domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the PerformanceTimeline methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Previously buffered events would be reported before method returns. See also: timelineEventAdded    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="PerformanceTimeline.enable", params=params, session_id=session_id)