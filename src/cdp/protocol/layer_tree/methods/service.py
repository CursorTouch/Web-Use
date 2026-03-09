"""CDP LayerTree Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class LayerTreeMethods:
    """
    Methods for the LayerTree domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the LayerTree methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def compositing_reasons(self, params: compositingReasonsParameters | None = None, session_id: str | None = None) -> compositingReasonsReturns:
        """
    Provides the reasons why the given layer was composited.    
        Args:
            params (compositingReasonsParameters, optional): Parameters for the compositingReasons method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    compositingReasonsReturns: The result of the compositingReasons call.
        """
        return await self.client.send(method="LayerTree.compositingReasons", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables compositing tree inspection.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="LayerTree.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables compositing tree inspection.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="LayerTree.enable", params=params, session_id=session_id)
    async def load_snapshot(self, params: loadSnapshotParameters | None = None, session_id: str | None = None) -> loadSnapshotReturns:
        """
    Returns the snapshot identifier.    
        Args:
            params (loadSnapshotParameters, optional): Parameters for the loadSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    loadSnapshotReturns: The result of the loadSnapshot call.
        """
        return await self.client.send(method="LayerTree.loadSnapshot", params=params, session_id=session_id)
    async def make_snapshot(self, params: makeSnapshotParameters | None = None, session_id: str | None = None) -> makeSnapshotReturns:
        """
    Returns the layer snapshot identifier.    
        Args:
            params (makeSnapshotParameters, optional): Parameters for the makeSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    makeSnapshotReturns: The result of the makeSnapshot call.
        """
        return await self.client.send(method="LayerTree.makeSnapshot", params=params, session_id=session_id)
    async def profile_snapshot(self, params: profileSnapshotParameters | None = None, session_id: str | None = None) -> profileSnapshotReturns:
        """
    No description available for profileSnapshot.    
        Args:
            params (profileSnapshotParameters, optional): Parameters for the profileSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    profileSnapshotReturns: The result of the profileSnapshot call.
        """
        return await self.client.send(method="LayerTree.profileSnapshot", params=params, session_id=session_id)
    async def release_snapshot(self, params: releaseSnapshotParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Releases layer snapshot captured by the back-end.    
        Args:
            params (releaseSnapshotParameters, optional): Parameters for the releaseSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the releaseSnapshot call.
        """
        return await self.client.send(method="LayerTree.releaseSnapshot", params=params, session_id=session_id)
    async def replay_snapshot(self, params: replaySnapshotParameters | None = None, session_id: str | None = None) -> replaySnapshotReturns:
        """
    Replays the layer snapshot and returns the resulting bitmap.    
        Args:
            params (replaySnapshotParameters, optional): Parameters for the replaySnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    replaySnapshotReturns: The result of the replaySnapshot call.
        """
        return await self.client.send(method="LayerTree.replaySnapshot", params=params, session_id=session_id)
    async def snapshot_command_log(self, params: snapshotCommandLogParameters | None = None, session_id: str | None = None) -> snapshotCommandLogReturns:
        """
    Replays the layer snapshot and returns canvas log.    
        Args:
            params (snapshotCommandLogParameters, optional): Parameters for the snapshotCommandLog method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    snapshotCommandLogReturns: The result of the snapshotCommandLog call.
        """
        return await self.client.send(method="LayerTree.snapshotCommandLog", params=params, session_id=session_id)