"""CDP CSS Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.css.types import CSSAnimationStyle
    from cdp.protocol.css.types import CSSAtRule
    from cdp.protocol.css.types import CSSComputedStyleProperty
    from cdp.protocol.css.types import CSSContainerQuery
    from cdp.protocol.css.types import CSSFunctionRule
    from cdp.protocol.css.types import CSSKeyframesRule
    from cdp.protocol.css.types import CSSLayerData
    from cdp.protocol.css.types import CSSMedia
    from cdp.protocol.css.types import CSSNavigation
    from cdp.protocol.css.types import CSSPositionTryRule
    from cdp.protocol.css.types import CSSProperty
    from cdp.protocol.css.types import CSSPropertyRegistration
    from cdp.protocol.css.types import CSSPropertyRule
    from cdp.protocol.css.types import CSSRule
    from cdp.protocol.css.types import CSSScope
    from cdp.protocol.css.types import CSSStyle
    from cdp.protocol.css.types import CSSSupports
    from cdp.protocol.css.types import ComputedStyleExtraFields
    from cdp.protocol.css.types import InheritedAnimatedStyleEntry
    from cdp.protocol.css.types import InheritedPseudoElementMatches
    from cdp.protocol.css.types import InheritedStyleEntry
    from cdp.protocol.css.types import PlatformFontUsage
    from cdp.protocol.css.types import PseudoElementMatches
    from cdp.protocol.css.types import RuleMatch
    from cdp.protocol.css.types import RuleUsage
    from cdp.protocol.css.types import SelectorList
    from cdp.protocol.css.types import SourceRange
    from cdp.protocol.css.types import StyleDeclarationEdit
    from cdp.protocol.css.types import Value
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom.types import PseudoType
    from cdp.protocol.dom.types import StyleSheetId
    from cdp.protocol.page.types import FrameId

class addRuleParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    """The css style sheet identifier where a new rule should be inserted."""
    ruleText: str
    """The text of a new rule."""
    location: SourceRange
    """Text position of a new rule in the target style sheet."""
    nodeForPropertySyntaxValidation: NotRequired[NodeId]
    """NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example."""
class collectClassNamesParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
class createStyleSheetParameters(TypedDict, total=True):
    frameId: FrameId
    """Identifier of the frame where "via-inspector" stylesheet should be created."""
    force: NotRequired[bool]
    """If true, creates a new stylesheet for every call. If false, returns a stylesheet previously created by a call with force=false for the frame's document if it exists or creates a new stylesheet (default: false)."""


class forcePseudoStateParameters(TypedDict, total=True):
    nodeId: NodeId
    """The element id for which to force the pseudo state."""
    forcedPseudoClasses: List[str]
    """Element pseudo classes to force when computing the element's style."""
class forceStartingStyleParameters(TypedDict, total=True):
    nodeId: NodeId
    """The element id for which to force the starting-style state."""
    forced: bool
    """Boolean indicating if this is on or off."""
class getBackgroundColorsParameters(TypedDict, total=True):
    nodeId: NodeId
    """Id of the node to get background colors for."""
class getComputedStyleForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
class resolveValuesParameters(TypedDict, total=True):
    values: List[str]
    """Cascade-dependent keywords (revert/revert-layer) do not work."""
    nodeId: NodeId
    """Id of the node in whose context the expression is evaluated"""
    propertyName: NotRequired[str]
    """Only longhands and custom property names are accepted."""
    pseudoType: NotRequired[PseudoType]
    """Pseudo element type, only works for pseudo elements that generate elements in the tree, such as ::before and ::after."""
    pseudoIdentifier: NotRequired[str]
    """Pseudo element custom ident."""
class getLonghandPropertiesParameters(TypedDict, total=True):
    shorthandName: str
    value: str
class getInlineStylesForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
class getAnimatedStylesForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
class getMatchedStylesForNodeParameters(TypedDict, total=True):
    nodeId: NodeId


class getPlatformFontsForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
class getStyleSheetTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
class getLayersForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
class getLocationForSelectorParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    selectorText: str
class trackComputedStyleUpdatesForNodeParameters(TypedDict, total=False):
    nodeId: NotRequired[NodeId]
class trackComputedStyleUpdatesParameters(TypedDict, total=True):
    propertiesToTrack: List[CSSComputedStyleProperty]

class setEffectivePropertyValueForNodeParameters(TypedDict, total=True):
    nodeId: NodeId
    """The element id for which to set property."""
    propertyName: str
    value: str
class setPropertyRulePropertyNameParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    propertyName: str
class setKeyframeKeyParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    keyText: str
class setMediaTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    text: str
class setContainerQueryTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    text: str
class setSupportsTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    text: str
class setNavigationTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    text: str
class setScopeTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    text: str
class setRuleSelectorParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    range: SourceRange
    selector: str
class setStyleSheetTextParameters(TypedDict, total=True):
    styleSheetId: StyleSheetId
    text: str
class setStyleTextsParameters(TypedDict, total=True):
    edits: List[StyleDeclarationEdit]
    nodeForPropertySyntaxValidation: NotRequired[NodeId]
    """NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example."""



class setLocalFontsEnabledParameters(TypedDict, total=True):
    enabled: bool
    """Whether rendering of local fonts is enabled."""
class addRuleReturns(TypedDict):
    rule: CSSRule
    """The newly created rule."""
class collectClassNamesReturns(TypedDict):
    classNames: List[str]
    """Class name list."""
class createStyleSheetReturns(TypedDict):
    styleSheetId: StyleSheetId
    """Identifier of the created "via-inspector" stylesheet."""




class getBackgroundColorsReturns(TypedDict):
    backgroundColors: List[str]
    """The range of background colors behind this element, if it contains any visible text. If no visible text is present, this will be undefined. In the case of a flat background color, this will consist of simply that color. In the case of a gradient, this will consist of each of the color stops. For anything more complicated, this will be an empty array. Images will be ignored (as if the image had failed to load)."""
    computedFontSize: str
    """The computed font size for this node, as a CSS computed value string (e.g. '12px')."""
    computedFontWeight: str
    """The computed font weight for this node, as a CSS computed value string (e.g. 'normal' or '100')."""
class getComputedStyleForNodeReturns(TypedDict):
    computedStyle: List[CSSComputedStyleProperty]
    """Computed style for the specified DOM node."""
    extraFields: ComputedStyleExtraFields
    """A list of non-standard "extra fields" which blink stores alongside each computed style."""
class resolveValuesReturns(TypedDict):
    results: List[str]
class getLonghandPropertiesReturns(TypedDict):
    longhandProperties: List[CSSProperty]
class getInlineStylesForNodeReturns(TypedDict):
    inlineStyle: CSSStyle
    """Inline style for the specified DOM node."""
    attributesStyle: CSSStyle
    """Attribute-defined element style (e.g. resulting from "width=20 height=100%")."""
class getAnimatedStylesForNodeReturns(TypedDict):
    animationStyles: List[CSSAnimationStyle]
    """Styles coming from animations."""
    transitionsStyle: CSSStyle
    """Style coming from transitions."""
    inherited: List[InheritedAnimatedStyleEntry]
    """Inherited style entries for animationsStyle and transitionsStyle from the inheritance chain of the element."""
class getMatchedStylesForNodeReturns(TypedDict):
    inlineStyle: CSSStyle
    """Inline style for the specified DOM node."""
    attributesStyle: CSSStyle
    """Attribute-defined element style (e.g. resulting from "width=20 height=100%")."""
    matchedCSSRules: List[RuleMatch]
    """CSS rules matching this node, from all applicable stylesheets."""
    pseudoElements: List[PseudoElementMatches]
    """Pseudo style matches for this node."""
    inherited: List[InheritedStyleEntry]
    """A chain of inherited styles (from the immediate node parent up to the DOM tree root)."""
    inheritedPseudoElements: List[InheritedPseudoElementMatches]
    """A chain of inherited pseudo element styles (from the immediate node parent up to the DOM tree root)."""
    cssKeyframesRules: List[CSSKeyframesRule]
    """A list of CSS keyframed animations matching this node."""
    cssPositionTryRules: List[CSSPositionTryRule]
    """A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property."""
    activePositionFallbackIndex: int
    """Index of the active fallback in the applied position-try-fallback property, will not be set if there is no active position-try fallback."""
    cssPropertyRules: List[CSSPropertyRule]
    """A list of CSS at-property rules matching this node."""
    cssPropertyRegistrations: List[CSSPropertyRegistration]
    """A list of CSS property registrations matching this node."""
    cssAtRules: List[CSSAtRule]
    """A list of simple @rules matching this node or its pseudo-elements."""
    parentLayoutNodeId: NodeId
    """Id of the first parent element that does not have display: contents."""
    cssFunctionRules: List[CSSFunctionRule]
    """A list of CSS at-function rules referenced by styles of this node."""
class getEnvironmentVariablesReturns(TypedDict):
    environmentVariables: Dict[str, Any]
class getMediaQueriesReturns(TypedDict):
    medias: List[CSSMedia]
class getPlatformFontsForNodeReturns(TypedDict):
    fonts: List[PlatformFontUsage]
    """Usage statistics for every employed platform font."""
class getStyleSheetTextReturns(TypedDict):
    text: str
    """The stylesheet text."""
class getLayersForNodeReturns(TypedDict):
    rootLayer: CSSLayerData
class getLocationForSelectorReturns(TypedDict):
    ranges: List[SourceRange]


class takeComputedStyleUpdatesReturns(TypedDict):
    nodeIds: List[NodeId]
    """The list of node Ids that have their tracked computed styles updated."""

class setPropertyRulePropertyNameReturns(TypedDict):
    propertyName: Value
    """The resulting key text after modification."""
class setKeyframeKeyReturns(TypedDict):
    keyText: Value
    """The resulting key text after modification."""
class setMediaTextReturns(TypedDict):
    media: CSSMedia
    """The resulting CSS media rule after modification."""
class setContainerQueryTextReturns(TypedDict):
    containerQuery: CSSContainerQuery
    """The resulting CSS container query rule after modification."""
class setSupportsTextReturns(TypedDict):
    supports: CSSSupports
    """The resulting CSS Supports rule after modification."""
class setNavigationTextReturns(TypedDict):
    navigation: CSSNavigation
    """The resulting CSS Navigation rule after modification."""
class setScopeTextReturns(TypedDict):
    scope: CSSScope
    """The resulting CSS Scope rule after modification."""
class setRuleSelectorReturns(TypedDict):
    selectorList: SelectorList
    """The resulting selector list after modification."""
class setStyleSheetTextReturns(TypedDict):
    sourceMapURL: str
    """URL of source map associated with script (if any)."""
class setStyleTextsReturns(TypedDict):
    styles: List[CSSStyle]
    """The resulting styles after modification."""

class stopRuleUsageTrackingReturns(TypedDict):
    ruleUsage: List[RuleUsage]
class takeCoverageDeltaReturns(TypedDict):
    coverage: List[RuleUsage]
    timestamp: float
    """Monotonically increasing time, in seconds."""