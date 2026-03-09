"""CDP Performance Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PerformanceMethods:
    """
    Methods for the Performance domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Performance methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disable collecting and reporting metrics.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Performance.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable collecting and reporting metrics.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Performance.enable", params=params, session_id=session_id)
    async def get_metrics(self, params: getMetricsParameters | None = None, session_id: str | None = None) -> getMetricsReturns:
        """
    Retrieve current values of run-time metrics.    
        Args:
            params (getMetricsParameters, optional): Parameters for the getMetrics method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getMetricsReturns: The result of the getMetrics call.
        """
        return await self.client.send(method="Performance.getMetrics", params=params, session_id=session_id)