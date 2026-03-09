"""CDP DOM Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class DOMMethods:
    """
    Methods for the DOM domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the DOM methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def collect_class_names_from_subtree(self, params: collectClassNamesFromSubtreeParameters | None = None, session_id: str | None = None) -> collectClassNamesFromSubtreeReturns:
        """
    Collects class names for the node with given id and all of it's child nodes.    
        Args:
            params (collectClassNamesFromSubtreeParameters, optional): Parameters for the collectClassNamesFromSubtree method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    collectClassNamesFromSubtreeReturns: The result of the collectClassNamesFromSubtree call.
        """
        return await self.client.send(method="DOM.collectClassNamesFromSubtree", params=params, session_id=session_id)
    async def copy_to(self, params: copyToParameters | None = None, session_id: str | None = None) -> copyToReturns:
        """
    Creates a deep copy of the specified node and places it into the target container before the given anchor.    
        Args:
            params (copyToParameters, optional): Parameters for the copyTo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    copyToReturns: The result of the copyTo call.
        """
        return await self.client.send(method="DOM.copyTo", params=params, session_id=session_id)
    async def describe_node(self, params: describeNodeParameters | None = None, session_id: str | None = None) -> describeNodeReturns:
        """
    Describes node given its id, does not require domain to be enabled. Does not start tracking any objects, can be used for automation.    
        Args:
            params (describeNodeParameters, optional): Parameters for the describeNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    describeNodeReturns: The result of the describeNode call.
        """
        return await self.client.send(method="DOM.describeNode", params=params, session_id=session_id)
    async def scroll_into_view_if_needed(self, params: scrollIntoViewIfNeededParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Scrolls the specified rect of the given node into view if not already visible. Note: exactly one between nodeId, backendNodeId and objectId should be passed to identify the node.    
        Args:
            params (scrollIntoViewIfNeededParameters, optional): Parameters for the scrollIntoViewIfNeeded method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the scrollIntoViewIfNeeded call.
        """
        return await self.client.send(method="DOM.scrollIntoViewIfNeeded", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables DOM agent for the given page.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="DOM.disable", params=params, session_id=session_id)
    async def discard_search_results(self, params: discardSearchResultsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Discards search results from the session with the given id. `getSearchResults` should no longer be called for that search.    
        Args:
            params (discardSearchResultsParameters, optional): Parameters for the discardSearchResults method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the discardSearchResults call.
        """
        return await self.client.send(method="DOM.discardSearchResults", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables DOM agent for the given page.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="DOM.enable", params=params, session_id=session_id)
    async def focus(self, params: focusParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Focuses the given element.    
        Args:
            params (focusParameters, optional): Parameters for the focus method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the focus call.
        """
        return await self.client.send(method="DOM.focus", params=params, session_id=session_id)
    async def get_attributes(self, params: getAttributesParameters | None = None, session_id: str | None = None) -> getAttributesReturns:
        """
    Returns attributes for the specified node.    
        Args:
            params (getAttributesParameters, optional): Parameters for the getAttributes method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAttributesReturns: The result of the getAttributes call.
        """
        return await self.client.send(method="DOM.getAttributes", params=params, session_id=session_id)
    async def get_box_model(self, params: getBoxModelParameters | None = None, session_id: str | None = None) -> getBoxModelReturns:
        """
    Returns boxes for the given node.    
        Args:
            params (getBoxModelParameters, optional): Parameters for the getBoxModel method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getBoxModelReturns: The result of the getBoxModel call.
        """
        return await self.client.send(method="DOM.getBoxModel", params=params, session_id=session_id)
    async def get_content_quads(self, params: getContentQuadsParameters | None = None, session_id: str | None = None) -> getContentQuadsReturns:
        """
    Returns quads that describe node position on the page. This method might return multiple quads for inline nodes.    
        Args:
            params (getContentQuadsParameters, optional): Parameters for the getContentQuads method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getContentQuadsReturns: The result of the getContentQuads call.
        """
        return await self.client.send(method="DOM.getContentQuads", params=params, session_id=session_id)
    async def get_document(self, params: getDocumentParameters | None = None, session_id: str | None = None) -> getDocumentReturns:
        """
    Returns the root DOM node (and optionally the subtree) to the caller. Implicitly enables the DOM domain events for the current target.    
        Args:
            params (getDocumentParameters, optional): Parameters for the getDocument method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getDocumentReturns: The result of the getDocument call.
        """
        return await self.client.send(method="DOM.getDocument", params=params, session_id=session_id)
    async def get_nodes_for_subtree_by_style(self, params: getNodesForSubtreeByStyleParameters | None = None, session_id: str | None = None) -> getNodesForSubtreeByStyleReturns:
        """
    Finds nodes with a given computed style in a subtree.    
        Args:
            params (getNodesForSubtreeByStyleParameters, optional): Parameters for the getNodesForSubtreeByStyle method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getNodesForSubtreeByStyleReturns: The result of the getNodesForSubtreeByStyle call.
        """
        return await self.client.send(method="DOM.getNodesForSubtreeByStyle", params=params, session_id=session_id)
    async def get_node_for_location(self, params: getNodeForLocationParameters | None = None, session_id: str | None = None) -> getNodeForLocationReturns:
        """
    Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is either returned or not.    
        Args:
            params (getNodeForLocationParameters, optional): Parameters for the getNodeForLocation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getNodeForLocationReturns: The result of the getNodeForLocation call.
        """
        return await self.client.send(method="DOM.getNodeForLocation", params=params, session_id=session_id)
    async def get_outer_html(self, params: getOuterHTMLParameters | None = None, session_id: str | None = None) -> getOuterHTMLReturns:
        """
    Returns node's HTML markup.    
        Args:
            params (getOuterHTMLParameters, optional): Parameters for the getOuterHTML method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getOuterHTMLReturns: The result of the getOuterHTML call.
        """
        return await self.client.send(method="DOM.getOuterHTML", params=params, session_id=session_id)
    async def get_relayout_boundary(self, params: getRelayoutBoundaryParameters | None = None, session_id: str | None = None) -> getRelayoutBoundaryReturns:
        """
    Returns the id of the nearest ancestor that is a relayout boundary.    
        Args:
            params (getRelayoutBoundaryParameters, optional): Parameters for the getRelayoutBoundary method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getRelayoutBoundaryReturns: The result of the getRelayoutBoundary call.
        """
        return await self.client.send(method="DOM.getRelayoutBoundary", params=params, session_id=session_id)
    async def get_search_results(self, params: getSearchResultsParameters | None = None, session_id: str | None = None) -> getSearchResultsReturns:
        """
    Returns search results from given `fromIndex` to given `toIndex` from the search with the given identifier.    
        Args:
            params (getSearchResultsParameters, optional): Parameters for the getSearchResults method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getSearchResultsReturns: The result of the getSearchResults call.
        """
        return await self.client.send(method="DOM.getSearchResults", params=params, session_id=session_id)
    async def hide_highlight(self, params: hideHighlightParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Hides any highlight.    
        Args:
            params (hideHighlightParameters, optional): Parameters for the hideHighlight method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the hideHighlight call.
        """
        return await self.client.send(method="DOM.hideHighlight", params=params, session_id=session_id)
    async def highlight_node(self, params: highlightNodeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights DOM node.    
        Args:
            params (highlightNodeParameters, optional): Parameters for the highlightNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the highlightNode call.
        """
        return await self.client.send(method="DOM.highlightNode", params=params, session_id=session_id)
    async def highlight_rect(self, params: highlightRectParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights given rectangle.    
        Args:
            params (highlightRectParameters, optional): Parameters for the highlightRect method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the highlightRect call.
        """
        return await self.client.send(method="DOM.highlightRect", params=params, session_id=session_id)
    async def mark_undoable_state(self, params: markUndoableStateParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Marks last undoable state.    
        Args:
            params (markUndoableStateParameters, optional): Parameters for the markUndoableState method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the markUndoableState call.
        """
        return await self.client.send(method="DOM.markUndoableState", params=params, session_id=session_id)
    async def move_to(self, params: moveToParameters | None = None, session_id: str | None = None) -> moveToReturns:
        """
    Moves node into the new container, places it before the given anchor.    
        Args:
            params (moveToParameters, optional): Parameters for the moveTo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    moveToReturns: The result of the moveTo call.
        """
        return await self.client.send(method="DOM.moveTo", params=params, session_id=session_id)
    async def perform_search(self, params: performSearchParameters | None = None, session_id: str | None = None) -> performSearchReturns:
        """
    Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or `cancelSearch` to end this search session.    
        Args:
            params (performSearchParameters, optional): Parameters for the performSearch method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    performSearchReturns: The result of the performSearch call.
        """
        return await self.client.send(method="DOM.performSearch", params=params, session_id=session_id)
    async def push_node_by_path_to_frontend(self, params: pushNodeByPathToFrontendParameters | None = None, session_id: str | None = None) -> pushNodeByPathToFrontendReturns:
        """
    Requests that the node is sent to the caller given its path. // FIXME, use XPath    
        Args:
            params (pushNodeByPathToFrontendParameters, optional): Parameters for the pushNodeByPathToFrontend method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    pushNodeByPathToFrontendReturns: The result of the pushNodeByPathToFrontend call.
        """
        return await self.client.send(method="DOM.pushNodeByPathToFrontend", params=params, session_id=session_id)
    async def push_nodes_by_backend_ids_to_frontend(self, params: pushNodesByBackendIdsToFrontendParameters | None = None, session_id: str | None = None) -> pushNodesByBackendIdsToFrontendReturns:
        """
    Requests that a batch of nodes is sent to the caller given their backend node ids.    
        Args:
            params (pushNodesByBackendIdsToFrontendParameters, optional): Parameters for the pushNodesByBackendIdsToFrontend method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    pushNodesByBackendIdsToFrontendReturns: The result of the pushNodesByBackendIdsToFrontend call.
        """
        return await self.client.send(method="DOM.pushNodesByBackendIdsToFrontend", params=params, session_id=session_id)
    async def query_selector(self, params: querySelectorParameters | None = None, session_id: str | None = None) -> querySelectorReturns:
        """
    Executes `querySelector` on a given node.    
        Args:
            params (querySelectorParameters, optional): Parameters for the querySelector method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    querySelectorReturns: The result of the querySelector call.
        """
        return await self.client.send(method="DOM.querySelector", params=params, session_id=session_id)
    async def query_selector_all(self, params: querySelectorAllParameters | None = None, session_id: str | None = None) -> querySelectorAllReturns:
        """
    Executes `querySelectorAll` on a given node.    
        Args:
            params (querySelectorAllParameters, optional): Parameters for the querySelectorAll method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    querySelectorAllReturns: The result of the querySelectorAll call.
        """
        return await self.client.send(method="DOM.querySelectorAll", params=params, session_id=session_id)
    async def get_top_layer_elements(self, params: getTopLayerElementsParameters | None = None, session_id: str | None = None) -> getTopLayerElementsReturns:
        """
    Returns NodeIds of current top layer elements. Top layer is rendered closest to the user within a viewport, therefore its elements always appear on top of all other content.    
        Args:
            params (getTopLayerElementsParameters, optional): Parameters for the getTopLayerElements method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getTopLayerElementsReturns: The result of the getTopLayerElements call.
        """
        return await self.client.send(method="DOM.getTopLayerElements", params=params, session_id=session_id)
    async def get_element_by_relation(self, params: getElementByRelationParameters | None = None, session_id: str | None = None) -> getElementByRelationReturns:
        """
    Returns the NodeId of the matched element according to certain relations.    
        Args:
            params (getElementByRelationParameters, optional): Parameters for the getElementByRelation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getElementByRelationReturns: The result of the getElementByRelation call.
        """
        return await self.client.send(method="DOM.getElementByRelation", params=params, session_id=session_id)
    async def redo(self, params: redoParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Re-does the last undone action.    
        Args:
            params (redoParameters, optional): Parameters for the redo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the redo call.
        """
        return await self.client.send(method="DOM.redo", params=params, session_id=session_id)
    async def remove_attribute(self, params: removeAttributeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes attribute with given name from an element with given id.    
        Args:
            params (removeAttributeParameters, optional): Parameters for the removeAttribute method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeAttribute call.
        """
        return await self.client.send(method="DOM.removeAttribute", params=params, session_id=session_id)
    async def remove_node(self, params: removeNodeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes node with given id.    
        Args:
            params (removeNodeParameters, optional): Parameters for the removeNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeNode call.
        """
        return await self.client.send(method="DOM.removeNode", params=params, session_id=session_id)
    async def request_child_nodes(self, params: requestChildNodesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that children of the node with given id are returned to the caller in form of `setChildNodes` events where not only immediate children are retrieved, but all children down to the specified depth.    
        Args:
            params (requestChildNodesParameters, optional): Parameters for the requestChildNodes method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the requestChildNodes call.
        """
        return await self.client.send(method="DOM.requestChildNodes", params=params, session_id=session_id)
    async def request_node(self, params: requestNodeParameters | None = None, session_id: str | None = None) -> requestNodeReturns:
        """
    Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of `setChildNodes` notifications.    
        Args:
            params (requestNodeParameters, optional): Parameters for the requestNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    requestNodeReturns: The result of the requestNode call.
        """
        return await self.client.send(method="DOM.requestNode", params=params, session_id=session_id)
    async def resolve_node(self, params: resolveNodeParameters | None = None, session_id: str | None = None) -> resolveNodeReturns:
        """
    Resolves the JavaScript node object for a given NodeId or BackendNodeId.    
        Args:
            params (resolveNodeParameters, optional): Parameters for the resolveNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    resolveNodeReturns: The result of the resolveNode call.
        """
        return await self.client.send(method="DOM.resolveNode", params=params, session_id=session_id)
    async def set_attribute_value(self, params: setAttributeValueParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets attribute for an element with given id.    
        Args:
            params (setAttributeValueParameters, optional): Parameters for the setAttributeValue method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAttributeValue call.
        """
        return await self.client.send(method="DOM.setAttributeValue", params=params, session_id=session_id)
    async def set_attributes_as_text(self, params: setAttributesAsTextParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs.    
        Args:
            params (setAttributesAsTextParameters, optional): Parameters for the setAttributesAsText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAttributesAsText call.
        """
        return await self.client.send(method="DOM.setAttributesAsText", params=params, session_id=session_id)
    async def set_file_input_files(self, params: setFileInputFilesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets files for the given file input element.    
        Args:
            params (setFileInputFilesParameters, optional): Parameters for the setFileInputFiles method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setFileInputFiles call.
        """
        return await self.client.send(method="DOM.setFileInputFiles", params=params, session_id=session_id)
    async def set_node_stack_traces_enabled(self, params: setNodeStackTracesEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled.    
        Args:
            params (setNodeStackTracesEnabledParameters, optional): Parameters for the setNodeStackTracesEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setNodeStackTracesEnabled call.
        """
        return await self.client.send(method="DOM.setNodeStackTracesEnabled", params=params, session_id=session_id)
    async def get_node_stack_traces(self, params: getNodeStackTracesParameters | None = None, session_id: str | None = None) -> getNodeStackTracesReturns:
        """
    Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation.    
        Args:
            params (getNodeStackTracesParameters, optional): Parameters for the getNodeStackTraces method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getNodeStackTracesReturns: The result of the getNodeStackTraces call.
        """
        return await self.client.send(method="DOM.getNodeStackTraces", params=params, session_id=session_id)
    async def get_file_info(self, params: getFileInfoParameters | None = None, session_id: str | None = None) -> getFileInfoReturns:
        """
    Returns file information for the given File wrapper.    
        Args:
            params (getFileInfoParameters, optional): Parameters for the getFileInfo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getFileInfoReturns: The result of the getFileInfo call.
        """
        return await self.client.send(method="DOM.getFileInfo", params=params, session_id=session_id)
    async def get_detached_dom_nodes(self, params: getDetachedDomNodesParameters | None = None, session_id: str | None = None) -> getDetachedDomNodesReturns:
        """
    Returns list of detached nodes    
        Args:
            params (getDetachedDomNodesParameters, optional): Parameters for the getDetachedDomNodes method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getDetachedDomNodesReturns: The result of the getDetachedDomNodes call.
        """
        return await self.client.send(method="DOM.getDetachedDomNodes", params=params, session_id=session_id)
    async def set_inspected_node(self, params: setInspectedNodeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).    
        Args:
            params (setInspectedNodeParameters, optional): Parameters for the setInspectedNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setInspectedNode call.
        """
        return await self.client.send(method="DOM.setInspectedNode", params=params, session_id=session_id)
    async def set_node_name(self, params: setNodeNameParameters | None = None, session_id: str | None = None) -> setNodeNameReturns:
        """
    Sets node name for a node with given id.    
        Args:
            params (setNodeNameParameters, optional): Parameters for the setNodeName method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setNodeNameReturns: The result of the setNodeName call.
        """
        return await self.client.send(method="DOM.setNodeName", params=params, session_id=session_id)
    async def set_node_value(self, params: setNodeValueParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets node value for a node with given id.    
        Args:
            params (setNodeValueParameters, optional): Parameters for the setNodeValue method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setNodeValue call.
        """
        return await self.client.send(method="DOM.setNodeValue", params=params, session_id=session_id)
    async def set_outer_html(self, params: setOuterHTMLParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets node HTML markup, returns new node id.    
        Args:
            params (setOuterHTMLParameters, optional): Parameters for the setOuterHTML method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setOuterHTML call.
        """
        return await self.client.send(method="DOM.setOuterHTML", params=params, session_id=session_id)
    async def undo(self, params: undoParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Undoes the last performed action.    
        Args:
            params (undoParameters, optional): Parameters for the undo method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the undo call.
        """
        return await self.client.send(method="DOM.undo", params=params, session_id=session_id)
    async def get_frame_owner(self, params: getFrameOwnerParameters | None = None, session_id: str | None = None) -> getFrameOwnerReturns:
        """
    Returns iframe node that owns iframe with the given domain.    
        Args:
            params (getFrameOwnerParameters, optional): Parameters for the getFrameOwner method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getFrameOwnerReturns: The result of the getFrameOwner call.
        """
        return await self.client.send(method="DOM.getFrameOwner", params=params, session_id=session_id)
    async def get_container_for_node(self, params: getContainerForNodeParameters | None = None, session_id: str | None = None) -> getContainerForNodeReturns:
        """
    Returns the query container of the given node based on container query conditions: containerName, physical and logical axes, and whether it queries scroll-state or anchored elements. If no axes are provided and queriesScrollState is false, the style container is returned, which is the direct parent or the closest element with a matching container-name.    
        Args:
            params (getContainerForNodeParameters, optional): Parameters for the getContainerForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getContainerForNodeReturns: The result of the getContainerForNode call.
        """
        return await self.client.send(method="DOM.getContainerForNode", params=params, session_id=session_id)
    async def get_querying_descendants_for_container(self, params: getQueryingDescendantsForContainerParameters | None = None, session_id: str | None = None) -> getQueryingDescendantsForContainerReturns:
        """
    Returns the descendants of a container query container that have container queries against this container.    
        Args:
            params (getQueryingDescendantsForContainerParameters, optional): Parameters for the getQueryingDescendantsForContainer method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getQueryingDescendantsForContainerReturns: The result of the getQueryingDescendantsForContainer call.
        """
        return await self.client.send(method="DOM.getQueryingDescendantsForContainer", params=params, session_id=session_id)
    async def get_anchor_element(self, params: getAnchorElementParameters | None = None, session_id: str | None = None) -> getAnchorElementReturns:
        """
    Returns the target anchor element of the given anchor query according to https://www.w3.org/TR/css-anchor-position-1/#target.    
        Args:
            params (getAnchorElementParameters, optional): Parameters for the getAnchorElement method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAnchorElementReturns: The result of the getAnchorElement call.
        """
        return await self.client.send(method="DOM.getAnchorElement", params=params, session_id=session_id)
    async def force_show_popover(self, params: forceShowPopoverParameters | None = None, session_id: str | None = None) -> forceShowPopoverReturns:
        """
    When enabling, this API force-opens the popover identified by nodeId and keeps it open until disabled.    
        Args:
            params (forceShowPopoverParameters, optional): Parameters for the forceShowPopover method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    forceShowPopoverReturns: The result of the forceShowPopover call.
        """
        return await self.client.send(method="DOM.forceShowPopover", params=params, session_id=session_id)