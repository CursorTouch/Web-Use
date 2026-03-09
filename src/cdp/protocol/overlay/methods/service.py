"""CDP Overlay Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class OverlayMethods:
    """
    Methods for the Overlay domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Overlay methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables domain notifications.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Overlay.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables domain notifications.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Overlay.enable", params=params, session_id=session_id)
    async def get_highlight_object_for_test(self, params: getHighlightObjectForTestParameters | None = None, session_id: str | None = None) -> getHighlightObjectForTestReturns:
        """
    For testing.    
        Args:
            params (getHighlightObjectForTestParameters, optional): Parameters for the getHighlightObjectForTest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getHighlightObjectForTestReturns: The result of the getHighlightObjectForTest call.
        """
        return await self.client.send(method="Overlay.getHighlightObjectForTest", params=params, session_id=session_id)
    async def get_grid_highlight_objects_for_test(self, params: getGridHighlightObjectsForTestParameters | None = None, session_id: str | None = None) -> getGridHighlightObjectsForTestReturns:
        """
    For Persistent Grid testing.    
        Args:
            params (getGridHighlightObjectsForTestParameters, optional): Parameters for the getGridHighlightObjectsForTest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getGridHighlightObjectsForTestReturns: The result of the getGridHighlightObjectsForTest call.
        """
        return await self.client.send(method="Overlay.getGridHighlightObjectsForTest", params=params, session_id=session_id)
    async def get_source_order_highlight_object_for_test(self, params: getSourceOrderHighlightObjectForTestParameters | None = None, session_id: str | None = None) -> getSourceOrderHighlightObjectForTestReturns:
        """
    For Source Order Viewer testing.    
        Args:
            params (getSourceOrderHighlightObjectForTestParameters, optional): Parameters for the getSourceOrderHighlightObjectForTest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getSourceOrderHighlightObjectForTestReturns: The result of the getSourceOrderHighlightObjectForTest call.
        """
        return await self.client.send(method="Overlay.getSourceOrderHighlightObjectForTest", params=params, session_id=session_id)
    async def hide_highlight(self, params: hideHighlightParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Hides any highlight.    
        Args:
            params (hideHighlightParameters, optional): Parameters for the hideHighlight method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the hideHighlight call.
        """
        return await self.client.send(method="Overlay.hideHighlight", params=params, session_id=session_id)
    async def highlight_node(self, params: highlightNodeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.    
        Args:
            params (highlightNodeParameters, optional): Parameters for the highlightNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the highlightNode call.
        """
        return await self.client.send(method="Overlay.highlightNode", params=params, session_id=session_id)
    async def highlight_quad(self, params: highlightQuadParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights given quad. Coordinates are absolute with respect to the main frame viewport.    
        Args:
            params (highlightQuadParameters, optional): Parameters for the highlightQuad method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the highlightQuad call.
        """
        return await self.client.send(method="Overlay.highlightQuad", params=params, session_id=session_id)
    async def highlight_rect(self, params: highlightRectParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport. Issue: the method does not handle device pixel ratio (DPR) correctly. The coordinates currently have to be adjusted by the client if DPR is not 1 (see crbug.com/437807128).    
        Args:
            params (highlightRectParameters, optional): Parameters for the highlightRect method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the highlightRect call.
        """
        return await self.client.send(method="Overlay.highlightRect", params=params, session_id=session_id)
    async def highlight_source_order(self, params: highlightSourceOrderParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights the source order of the children of the DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.    
        Args:
            params (highlightSourceOrderParameters, optional): Parameters for the highlightSourceOrder method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the highlightSourceOrder call.
        """
        return await self.client.send(method="Overlay.highlightSourceOrder", params=params, session_id=session_id)
    async def set_inspect_mode(self, params: setInspectModeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection.    
        Args:
            params (setInspectModeParameters, optional): Parameters for the setInspectMode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setInspectMode call.
        """
        return await self.client.send(method="Overlay.setInspectMode", params=params, session_id=session_id)
    async def set_show_ad_highlights(self, params: setShowAdHighlightsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlights owner element of all frames detected to be ads.    
        Args:
            params (setShowAdHighlightsParameters, optional): Parameters for the setShowAdHighlights method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowAdHighlights call.
        """
        return await self.client.send(method="Overlay.setShowAdHighlights", params=params, session_id=session_id)
    async def set_paused_in_debugger_message(self, params: setPausedInDebuggerMessageParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setPausedInDebuggerMessage.    
        Args:
            params (setPausedInDebuggerMessageParameters, optional): Parameters for the setPausedInDebuggerMessage method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPausedInDebuggerMessage call.
        """
        return await self.client.send(method="Overlay.setPausedInDebuggerMessage", params=params, session_id=session_id)
    async def set_show_debug_borders(self, params: setShowDebugBordersParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that backend shows debug borders on layers    
        Args:
            params (setShowDebugBordersParameters, optional): Parameters for the setShowDebugBorders method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowDebugBorders call.
        """
        return await self.client.send(method="Overlay.setShowDebugBorders", params=params, session_id=session_id)
    async def set_show_fps_counter(self, params: setShowFPSCounterParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that backend shows the FPS counter    
        Args:
            params (setShowFPSCounterParameters, optional): Parameters for the setShowFPSCounter method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowFPSCounter call.
        """
        return await self.client.send(method="Overlay.setShowFPSCounter", params=params, session_id=session_id)
    async def set_show_grid_overlays(self, params: setShowGridOverlaysParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Highlight multiple elements with the CSS Grid overlay.    
        Args:
            params (setShowGridOverlaysParameters, optional): Parameters for the setShowGridOverlays method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowGridOverlays call.
        """
        return await self.client.send(method="Overlay.setShowGridOverlays", params=params, session_id=session_id)
    async def set_show_flex_overlays(self, params: setShowFlexOverlaysParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setShowFlexOverlays.    
        Args:
            params (setShowFlexOverlaysParameters, optional): Parameters for the setShowFlexOverlays method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowFlexOverlays call.
        """
        return await self.client.send(method="Overlay.setShowFlexOverlays", params=params, session_id=session_id)
    async def set_show_scroll_snap_overlays(self, params: setShowScrollSnapOverlaysParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setShowScrollSnapOverlays.    
        Args:
            params (setShowScrollSnapOverlaysParameters, optional): Parameters for the setShowScrollSnapOverlays method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowScrollSnapOverlays call.
        """
        return await self.client.send(method="Overlay.setShowScrollSnapOverlays", params=params, session_id=session_id)
    async def set_show_container_query_overlays(self, params: setShowContainerQueryOverlaysParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setShowContainerQueryOverlays.    
        Args:
            params (setShowContainerQueryOverlaysParameters, optional): Parameters for the setShowContainerQueryOverlays method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowContainerQueryOverlays call.
        """
        return await self.client.send(method="Overlay.setShowContainerQueryOverlays", params=params, session_id=session_id)
    async def set_show_inspected_element_anchor(self, params: setShowInspectedElementAnchorParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setShowInspectedElementAnchor.    
        Args:
            params (setShowInspectedElementAnchorParameters, optional): Parameters for the setShowInspectedElementAnchor method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowInspectedElementAnchor call.
        """
        return await self.client.send(method="Overlay.setShowInspectedElementAnchor", params=params, session_id=session_id)
    async def set_show_paint_rects(self, params: setShowPaintRectsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that backend shows paint rectangles    
        Args:
            params (setShowPaintRectsParameters, optional): Parameters for the setShowPaintRects method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowPaintRects call.
        """
        return await self.client.send(method="Overlay.setShowPaintRects", params=params, session_id=session_id)
    async def set_show_layout_shift_regions(self, params: setShowLayoutShiftRegionsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that backend shows layout shift regions    
        Args:
            params (setShowLayoutShiftRegionsParameters, optional): Parameters for the setShowLayoutShiftRegions method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowLayoutShiftRegions call.
        """
        return await self.client.send(method="Overlay.setShowLayoutShiftRegions", params=params, session_id=session_id)
    async def set_show_scroll_bottleneck_rects(self, params: setShowScrollBottleneckRectsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that backend shows scroll bottleneck rects    
        Args:
            params (setShowScrollBottleneckRectsParameters, optional): Parameters for the setShowScrollBottleneckRects method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowScrollBottleneckRects call.
        """
        return await self.client.send(method="Overlay.setShowScrollBottleneckRects", params=params, session_id=session_id)
    async def set_show_viewport_size_on_resize(self, params: setShowViewportSizeOnResizeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Paints viewport size upon main frame resize.    
        Args:
            params (setShowViewportSizeOnResizeParameters, optional): Parameters for the setShowViewportSizeOnResize method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowViewportSizeOnResize call.
        """
        return await self.client.send(method="Overlay.setShowViewportSizeOnResize", params=params, session_id=session_id)
    async def set_show_hinge(self, params: setShowHingeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Add a dual screen device hinge    
        Args:
            params (setShowHingeParameters, optional): Parameters for the setShowHinge method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowHinge call.
        """
        return await self.client.send(method="Overlay.setShowHinge", params=params, session_id=session_id)
    async def set_show_isolated_elements(self, params: setShowIsolatedElementsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Show elements in isolation mode with overlays.    
        Args:
            params (setShowIsolatedElementsParameters, optional): Parameters for the setShowIsolatedElements method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowIsolatedElements call.
        """
        return await self.client.send(method="Overlay.setShowIsolatedElements", params=params, session_id=session_id)
    async def set_show_window_controls_overlay(self, params: setShowWindowControlsOverlayParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Show Window Controls Overlay for PWA    
        Args:
            params (setShowWindowControlsOverlayParameters, optional): Parameters for the setShowWindowControlsOverlay method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setShowWindowControlsOverlay call.
        """
        return await self.client.send(method="Overlay.setShowWindowControlsOverlay", params=params, session_id=session_id)