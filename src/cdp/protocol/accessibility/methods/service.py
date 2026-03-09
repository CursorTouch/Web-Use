"""CDP Accessibility Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class AccessibilityMethods:
    """
    Methods for the Accessibility domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Accessibility methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables the accessibility domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Accessibility.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls. This turns on accessibility for the page, which can impact performance until accessibility is disabled.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Accessibility.enable", params=params, session_id=session_id)
    async def get_partial_ax_tree(self, params: getPartialAXTreeParameters | None = None, session_id: str | None = None) -> getPartialAXTreeReturns:
        """
    Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.    
        Args:
            params (getPartialAXTreeParameters, optional): Parameters for the getPartialAXTree method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getPartialAXTreeReturns: The result of the getPartialAXTree call.
        """
        return await self.client.send(method="Accessibility.getPartialAXTree", params=params, session_id=session_id)
    async def get_full_ax_tree(self, params: getFullAXTreeParameters | None = None, session_id: str | None = None) -> getFullAXTreeReturns:
        """
    Fetches the entire accessibility tree for the root Document    
        Args:
            params (getFullAXTreeParameters, optional): Parameters for the getFullAXTree method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getFullAXTreeReturns: The result of the getFullAXTree call.
        """
        return await self.client.send(method="Accessibility.getFullAXTree", params=params, session_id=session_id)
    async def get_root_ax_node(self, params: getRootAXNodeParameters | None = None, session_id: str | None = None) -> getRootAXNodeReturns:
        """
    Fetches the root node. Requires `enable()` to have been called previously.    
        Args:
            params (getRootAXNodeParameters, optional): Parameters for the getRootAXNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getRootAXNodeReturns: The result of the getRootAXNode call.
        """
        return await self.client.send(method="Accessibility.getRootAXNode", params=params, session_id=session_id)
    async def get_ax_node_and_ancestors(self, params: getAXNodeAndAncestorsParameters | None = None, session_id: str | None = None) -> getAXNodeAndAncestorsReturns:
        """
    Fetches a node and all ancestors up to and including the root. Requires `enable()` to have been called previously.    
        Args:
            params (getAXNodeAndAncestorsParameters, optional): Parameters for the getAXNodeAndAncestors method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAXNodeAndAncestorsReturns: The result of the getAXNodeAndAncestors call.
        """
        return await self.client.send(method="Accessibility.getAXNodeAndAncestors", params=params, session_id=session_id)
    async def get_child_ax_nodes(self, params: getChildAXNodesParameters | None = None, session_id: str | None = None) -> getChildAXNodesReturns:
        """
    Fetches a particular accessibility node by AXNodeId. Requires `enable()` to have been called previously.    
        Args:
            params (getChildAXNodesParameters, optional): Parameters for the getChildAXNodes method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getChildAXNodesReturns: The result of the getChildAXNodes call.
        """
        return await self.client.send(method="Accessibility.getChildAXNodes", params=params, session_id=session_id)
    async def query_ax_tree(self, params: queryAXTreeParameters | None = None, session_id: str | None = None) -> queryAXTreeReturns:
        """
    Query a DOM node's accessibility subtree for accessible name and role. This command computes the name and role for all nodes in the subtree, including those that are ignored for accessibility, and returns those that match the specified name and role. If no DOM node is specified, or the DOM node does not exist, the command returns an error. If neither `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree.    
        Args:
            params (queryAXTreeParameters, optional): Parameters for the queryAXTree method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    queryAXTreeReturns: The result of the queryAXTree call.
        """
        return await self.client.send(method="Accessibility.queryAXTree", params=params, session_id=session_id)