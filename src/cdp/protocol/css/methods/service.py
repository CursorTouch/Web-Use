"""CDP CSS Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class CSSMethods:
    """
    Methods for the CSS domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the CSS methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def add_rule(self, params: addRuleParameters | None = None, session_id: str | None = None) -> addRuleReturns:
        """
    Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified by `location`.    
        Args:
            params (addRuleParameters, optional): Parameters for the addRule method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    addRuleReturns: The result of the addRule call.
        """
        return await self.client.send(method="CSS.addRule", params=params, session_id=session_id)
    async def collect_class_names(self, params: collectClassNamesParameters | None = None, session_id: str | None = None) -> collectClassNamesReturns:
        """
    Returns all class names from specified stylesheet.    
        Args:
            params (collectClassNamesParameters, optional): Parameters for the collectClassNames method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    collectClassNamesReturns: The result of the collectClassNames call.
        """
        return await self.client.send(method="CSS.collectClassNames", params=params, session_id=session_id)
    async def create_style_sheet(self, params: createStyleSheetParameters | None = None, session_id: str | None = None) -> createStyleSheetReturns:
        """
    Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.    
        Args:
            params (createStyleSheetParameters, optional): Parameters for the createStyleSheet method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    createStyleSheetReturns: The result of the createStyleSheet call.
        """
        return await self.client.send(method="CSS.createStyleSheet", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables the CSS agent for the given page.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="CSS.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="CSS.enable", params=params, session_id=session_id)
    async def force_pseudo_state(self, params: forcePseudoStateParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser.    
        Args:
            params (forcePseudoStateParameters, optional): Parameters for the forcePseudoState method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the forcePseudoState call.
        """
        return await self.client.send(method="CSS.forcePseudoState", params=params, session_id=session_id)
    async def force_starting_style(self, params: forceStartingStyleParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Ensures that the given node is in its starting-style state.    
        Args:
            params (forceStartingStyleParameters, optional): Parameters for the forceStartingStyle method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the forceStartingStyle call.
        """
        return await self.client.send(method="CSS.forceStartingStyle", params=params, session_id=session_id)
    async def get_background_colors(self, params: getBackgroundColorsParameters | None = None, session_id: str | None = None) -> getBackgroundColorsReturns:
        """
    No description available for getBackgroundColors.    
        Args:
            params (getBackgroundColorsParameters, optional): Parameters for the getBackgroundColors method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getBackgroundColorsReturns: The result of the getBackgroundColors call.
        """
        return await self.client.send(method="CSS.getBackgroundColors", params=params, session_id=session_id)
    async def get_computed_style_for_node(self, params: getComputedStyleForNodeParameters | None = None, session_id: str | None = None) -> getComputedStyleForNodeReturns:
        """
    Returns the computed style for a DOM node identified by `nodeId`.    
        Args:
            params (getComputedStyleForNodeParameters, optional): Parameters for the getComputedStyleForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getComputedStyleForNodeReturns: The result of the getComputedStyleForNode call.
        """
        return await self.client.send(method="CSS.getComputedStyleForNode", params=params, session_id=session_id)
    async def resolve_values(self, params: resolveValuesParameters | None = None, session_id: str | None = None) -> resolveValuesReturns:
        """
    Resolve the specified values in the context of the provided element. For example, a value of '1em' is evaluated according to the computed 'font-size' of the element and a value 'calc(1px + 2px)' will be resolved to '3px'. If the `propertyName` was specified the `values` are resolved as if they were property's declaration. If a value cannot be parsed according to the provided property syntax, the value is parsed using combined syntax as if null `propertyName` was provided. If the value cannot be resolved even then, return the provided value without any changes. Note: this function currently does not resolve CSS random() function, it returns unmodified random() function parts.`    
        Args:
            params (resolveValuesParameters, optional): Parameters for the resolveValues method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    resolveValuesReturns: The result of the resolveValues call.
        """
        return await self.client.send(method="CSS.resolveValues", params=params, session_id=session_id)
    async def get_longhand_properties(self, params: getLonghandPropertiesParameters | None = None, session_id: str | None = None) -> getLonghandPropertiesReturns:
        """
    No description available for getLonghandProperties.    
        Args:
            params (getLonghandPropertiesParameters, optional): Parameters for the getLonghandProperties method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getLonghandPropertiesReturns: The result of the getLonghandProperties call.
        """
        return await self.client.send(method="CSS.getLonghandProperties", params=params, session_id=session_id)
    async def get_inline_styles_for_node(self, params: getInlineStylesForNodeParameters | None = None, session_id: str | None = None) -> getInlineStylesForNodeReturns:
        """
    Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by `nodeId`.    
        Args:
            params (getInlineStylesForNodeParameters, optional): Parameters for the getInlineStylesForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getInlineStylesForNodeReturns: The result of the getInlineStylesForNode call.
        """
        return await self.client.send(method="CSS.getInlineStylesForNode", params=params, session_id=session_id)
    async def get_animated_styles_for_node(self, params: getAnimatedStylesForNodeParameters | None = None, session_id: str | None = None) -> getAnimatedStylesForNodeReturns:
        """
    Returns the styles coming from animations & transitions including the animation & transition styles coming from inheritance chain.    
        Args:
            params (getAnimatedStylesForNodeParameters, optional): Parameters for the getAnimatedStylesForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAnimatedStylesForNodeReturns: The result of the getAnimatedStylesForNode call.
        """
        return await self.client.send(method="CSS.getAnimatedStylesForNode", params=params, session_id=session_id)
    async def get_matched_styles_for_node(self, params: getMatchedStylesForNodeParameters | None = None, session_id: str | None = None) -> getMatchedStylesForNodeReturns:
        """
    Returns requested styles for a DOM node identified by `nodeId`.    
        Args:
            params (getMatchedStylesForNodeParameters, optional): Parameters for the getMatchedStylesForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getMatchedStylesForNodeReturns: The result of the getMatchedStylesForNode call.
        """
        return await self.client.send(method="CSS.getMatchedStylesForNode", params=params, session_id=session_id)
    async def get_environment_variables(self, params: getEnvironmentVariablesParameters | None = None, session_id: str | None = None) -> getEnvironmentVariablesReturns:
        """
    Returns the values of the default UA-defined environment variables used in env()    
        Args:
            params (getEnvironmentVariablesParameters, optional): Parameters for the getEnvironmentVariables method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getEnvironmentVariablesReturns: The result of the getEnvironmentVariables call.
        """
        return await self.client.send(method="CSS.getEnvironmentVariables", params=params, session_id=session_id)
    async def get_media_queries(self, params: getMediaQueriesParameters | None = None, session_id: str | None = None) -> getMediaQueriesReturns:
        """
    Returns all media queries parsed by the rendering engine.    
        Args:
            params (getMediaQueriesParameters, optional): Parameters for the getMediaQueries method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getMediaQueriesReturns: The result of the getMediaQueries call.
        """
        return await self.client.send(method="CSS.getMediaQueries", params=params, session_id=session_id)
    async def get_platform_fonts_for_node(self, params: getPlatformFontsForNodeParameters | None = None, session_id: str | None = None) -> getPlatformFontsForNodeReturns:
        """
    Requests information about platform fonts which we used to render child TextNodes in the given node.    
        Args:
            params (getPlatformFontsForNodeParameters, optional): Parameters for the getPlatformFontsForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getPlatformFontsForNodeReturns: The result of the getPlatformFontsForNode call.
        """
        return await self.client.send(method="CSS.getPlatformFontsForNode", params=params, session_id=session_id)
    async def get_style_sheet_text(self, params: getStyleSheetTextParameters | None = None, session_id: str | None = None) -> getStyleSheetTextReturns:
        """
    Returns the current textual content for a stylesheet.    
        Args:
            params (getStyleSheetTextParameters, optional): Parameters for the getStyleSheetText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getStyleSheetTextReturns: The result of the getStyleSheetText call.
        """
        return await self.client.send(method="CSS.getStyleSheetText", params=params, session_id=session_id)
    async def get_layers_for_node(self, params: getLayersForNodeParameters | None = None, session_id: str | None = None) -> getLayersForNodeReturns:
        """
    Returns all layers parsed by the rendering engine for the tree scope of a node. Given a DOM element identified by nodeId, getLayersForNode returns the root layer for the nearest ancestor document or shadow root. The layer root contains the full layer tree for the tree scope and their ordering.    
        Args:
            params (getLayersForNodeParameters, optional): Parameters for the getLayersForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getLayersForNodeReturns: The result of the getLayersForNode call.
        """
        return await self.client.send(method="CSS.getLayersForNode", params=params, session_id=session_id)
    async def get_location_for_selector(self, params: getLocationForSelectorParameters | None = None, session_id: str | None = None) -> getLocationForSelectorReturns:
        """
    Given a CSS selector text and a style sheet ID, getLocationForSelector returns an array of locations of the CSS selector in the style sheet.    
        Args:
            params (getLocationForSelectorParameters, optional): Parameters for the getLocationForSelector method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getLocationForSelectorReturns: The result of the getLocationForSelector call.
        """
        return await self.client.send(method="CSS.getLocationForSelector", params=params, session_id=session_id)
    async def track_computed_style_updates_for_node(self, params: trackComputedStyleUpdatesForNodeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Starts tracking the given node for the computed style updates and whenever the computed style is updated for node, it queues a `computedStyleUpdated` event with throttling. There can only be 1 node tracked for computed style updates so passing a new node id removes tracking from the previous node. Pass `undefined` to disable tracking.    
        Args:
            params (trackComputedStyleUpdatesForNodeParameters, optional): Parameters for the trackComputedStyleUpdatesForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the trackComputedStyleUpdatesForNode call.
        """
        return await self.client.send(method="CSS.trackComputedStyleUpdatesForNode", params=params, session_id=session_id)
    async def track_computed_style_updates(self, params: trackComputedStyleUpdatesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Starts tracking the given computed styles for updates. The specified array of properties replaces the one previously specified. Pass empty array to disable tracking. Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified. The changes to computed style properties are only tracked for nodes pushed to the front-end by the DOM agent. If no changes to the tracked properties occur after the node has been pushed to the front-end, no updates will be issued for the node.    
        Args:
            params (trackComputedStyleUpdatesParameters, optional): Parameters for the trackComputedStyleUpdates method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the trackComputedStyleUpdates call.
        """
        return await self.client.send(method="CSS.trackComputedStyleUpdates", params=params, session_id=session_id)
    async def take_computed_style_updates(self, params: takeComputedStyleUpdatesParameters | None = None, session_id: str | None = None) -> takeComputedStyleUpdatesReturns:
        """
    Polls the next batch of computed style updates.    
        Args:
            params (takeComputedStyleUpdatesParameters, optional): Parameters for the takeComputedStyleUpdates method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    takeComputedStyleUpdatesReturns: The result of the takeComputedStyleUpdates call.
        """
        return await self.client.send(method="CSS.takeComputedStyleUpdates", params=params, session_id=session_id)
    async def set_effective_property_value_for_node(self, params: setEffectivePropertyValueForNodeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Find a rule with the given active property for the given node and set the new value for this property    
        Args:
            params (setEffectivePropertyValueForNodeParameters, optional): Parameters for the setEffectivePropertyValueForNode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setEffectivePropertyValueForNode call.
        """
        return await self.client.send(method="CSS.setEffectivePropertyValueForNode", params=params, session_id=session_id)
    async def set_property_rule_property_name(self, params: setPropertyRulePropertyNameParameters | None = None, session_id: str | None = None) -> setPropertyRulePropertyNameReturns:
        """
    Modifies the property rule property name.    
        Args:
            params (setPropertyRulePropertyNameParameters, optional): Parameters for the setPropertyRulePropertyName method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setPropertyRulePropertyNameReturns: The result of the setPropertyRulePropertyName call.
        """
        return await self.client.send(method="CSS.setPropertyRulePropertyName", params=params, session_id=session_id)
    async def set_keyframe_key(self, params: setKeyframeKeyParameters | None = None, session_id: str | None = None) -> setKeyframeKeyReturns:
        """
    Modifies the keyframe rule key text.    
        Args:
            params (setKeyframeKeyParameters, optional): Parameters for the setKeyframeKey method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setKeyframeKeyReturns: The result of the setKeyframeKey call.
        """
        return await self.client.send(method="CSS.setKeyframeKey", params=params, session_id=session_id)
    async def set_media_text(self, params: setMediaTextParameters | None = None, session_id: str | None = None) -> setMediaTextReturns:
        """
    Modifies the rule selector.    
        Args:
            params (setMediaTextParameters, optional): Parameters for the setMediaText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setMediaTextReturns: The result of the setMediaText call.
        """
        return await self.client.send(method="CSS.setMediaText", params=params, session_id=session_id)
    async def set_container_query_text(self, params: setContainerQueryTextParameters | None = None, session_id: str | None = None) -> setContainerQueryTextReturns:
        """
    Modifies the expression of a container query.    
        Args:
            params (setContainerQueryTextParameters, optional): Parameters for the setContainerQueryText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setContainerQueryTextReturns: The result of the setContainerQueryText call.
        """
        return await self.client.send(method="CSS.setContainerQueryText", params=params, session_id=session_id)
    async def set_supports_text(self, params: setSupportsTextParameters | None = None, session_id: str | None = None) -> setSupportsTextReturns:
        """
    Modifies the expression of a supports at-rule.    
        Args:
            params (setSupportsTextParameters, optional): Parameters for the setSupportsText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setSupportsTextReturns: The result of the setSupportsText call.
        """
        return await self.client.send(method="CSS.setSupportsText", params=params, session_id=session_id)
    async def set_navigation_text(self, params: setNavigationTextParameters | None = None, session_id: str | None = None) -> setNavigationTextReturns:
        """
    Modifies the expression of a navigation at-rule.    
        Args:
            params (setNavigationTextParameters, optional): Parameters for the setNavigationText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setNavigationTextReturns: The result of the setNavigationText call.
        """
        return await self.client.send(method="CSS.setNavigationText", params=params, session_id=session_id)
    async def set_scope_text(self, params: setScopeTextParameters | None = None, session_id: str | None = None) -> setScopeTextReturns:
        """
    Modifies the expression of a scope at-rule.    
        Args:
            params (setScopeTextParameters, optional): Parameters for the setScopeText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setScopeTextReturns: The result of the setScopeText call.
        """
        return await self.client.send(method="CSS.setScopeText", params=params, session_id=session_id)
    async def set_rule_selector(self, params: setRuleSelectorParameters | None = None, session_id: str | None = None) -> setRuleSelectorReturns:
        """
    Modifies the rule selector.    
        Args:
            params (setRuleSelectorParameters, optional): Parameters for the setRuleSelector method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setRuleSelectorReturns: The result of the setRuleSelector call.
        """
        return await self.client.send(method="CSS.setRuleSelector", params=params, session_id=session_id)
    async def set_style_sheet_text(self, params: setStyleSheetTextParameters | None = None, session_id: str | None = None) -> setStyleSheetTextReturns:
        """
    Sets the new stylesheet text.    
        Args:
            params (setStyleSheetTextParameters, optional): Parameters for the setStyleSheetText method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setStyleSheetTextReturns: The result of the setStyleSheetText call.
        """
        return await self.client.send(method="CSS.setStyleSheetText", params=params, session_id=session_id)
    async def set_style_texts(self, params: setStyleTextsParameters | None = None, session_id: str | None = None) -> setStyleTextsReturns:
        """
    Applies specified style edits one after another in the given order.    
        Args:
            params (setStyleTextsParameters, optional): Parameters for the setStyleTexts method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setStyleTextsReturns: The result of the setStyleTexts call.
        """
        return await self.client.send(method="CSS.setStyleTexts", params=params, session_id=session_id)
    async def start_rule_usage_tracking(self, params: startRuleUsageTrackingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables the selector recording.    
        Args:
            params (startRuleUsageTrackingParameters, optional): Parameters for the startRuleUsageTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startRuleUsageTracking call.
        """
        return await self.client.send(method="CSS.startRuleUsageTracking", params=params, session_id=session_id)
    async def stop_rule_usage_tracking(self, params: stopRuleUsageTrackingParameters | None = None, session_id: str | None = None) -> stopRuleUsageTrackingReturns:
        """
    Stop tracking rule usage and return the list of rules that were used since last call to `takeCoverageDelta` (or since start of coverage instrumentation).    
        Args:
            params (stopRuleUsageTrackingParameters, optional): Parameters for the stopRuleUsageTracking method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    stopRuleUsageTrackingReturns: The result of the stopRuleUsageTracking call.
        """
        return await self.client.send(method="CSS.stopRuleUsageTracking", params=params, session_id=session_id)
    async def take_coverage_delta(self, params: takeCoverageDeltaParameters | None = None, session_id: str | None = None) -> takeCoverageDeltaReturns:
        """
    Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation).    
        Args:
            params (takeCoverageDeltaParameters, optional): Parameters for the takeCoverageDelta method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    takeCoverageDeltaReturns: The result of the takeCoverageDelta call.
        """
        return await self.client.send(method="CSS.takeCoverageDelta", params=params, session_id=session_id)
    async def set_local_fonts_enabled(self, params: setLocalFontsEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables/disables rendering of local CSS fonts (enabled by default).    
        Args:
            params (setLocalFontsEnabledParameters, optional): Parameters for the setLocalFontsEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setLocalFontsEnabled call.
        """
        return await self.client.send(method="CSS.setLocalFontsEnabled", params=params, session_id=session_id)