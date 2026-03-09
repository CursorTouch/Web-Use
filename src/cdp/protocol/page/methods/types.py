"""CDP Page Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.debugger.types import SearchMatch
    from cdp.protocol.dom.types import Rect
    from cdp.protocol.io.types import StreamHandle
    from cdp.protocol.network.types import LoaderId
    from cdp.protocol.page.types import AdScriptAncestry
    from cdp.protocol.page.types import AppManifestError
    from cdp.protocol.page.types import AppManifestParsedProperties
    from cdp.protocol.page.types import CompilationCacheParams
    from cdp.protocol.page.types import FontFamilies
    from cdp.protocol.page.types import FontSizes
    from cdp.protocol.page.types import FrameId
    from cdp.protocol.page.types import FrameResourceTree
    from cdp.protocol.page.types import FrameTree
    from cdp.protocol.page.types import InstallabilityError
    from cdp.protocol.page.types import LayoutViewport
    from cdp.protocol.page.types import NavigationEntry
    from cdp.protocol.page.types import OriginTrial
    from cdp.protocol.page.types import PermissionsPolicyFeatureState
    from cdp.protocol.page.types import ReferrerPolicy
    from cdp.protocol.page.types import ScriptFontFamilies
    from cdp.protocol.page.types import ScriptIdentifier
    from cdp.protocol.page.types import TransitionType
    from cdp.protocol.page.types import Viewport
    from cdp.protocol.page.types import VisualViewport
    from cdp.protocol.page.types import WebAppManifest
    from cdp.protocol.runtime.types import ExecutionContextId

class addScriptToEvaluateOnNewDocumentParameters(TypedDict, total=True):
    source: str
    worldName: NotRequired[str]
    """If specified, creates an isolated world with the given name and evaluates given script in it. This world name will be used as the ExecutionContextDescription::name when the corresponding event is emitted."""
    includeCommandLineAPI: NotRequired[bool]
    """Specifies whether command line API should be available to the script, defaults to false."""
    runImmediately: NotRequired[bool]
    """If true, runs the script immediately on existing execution contexts or worlds. Default: false."""

class captureScreenshotParameters(TypedDict, total=False):
    format: NotRequired[Literal["jpeg", "png", "webp"]]
    """Image compression format (defaults to png)."""
    quality: NotRequired[int]
    """Compression quality from range [0..100] (jpeg only)."""
    clip: NotRequired[Viewport]
    """Capture the screenshot of a given region only."""
    fromSurface: NotRequired[bool]
    """Capture the screenshot from the surface, rather than the view. Defaults to true."""
    captureBeyondViewport: NotRequired[bool]
    """Capture the screenshot beyond the viewport. Defaults to false."""
    optimizeForSpeed: NotRequired[bool]
    """Optimize image encoding for speed, not for resulting size (defaults to false)"""
class captureSnapshotParameters(TypedDict, total=False):
    format: NotRequired[Literal["mhtml"]]
    """Format (defaults to mhtml)."""
class createIsolatedWorldParameters(TypedDict, total=True):
    frameId: FrameId
    """Id of the frame in which the isolated world should be created."""
    worldName: NotRequired[str]
    """An optional name which is reported in the Execution Context."""
    grantUniveralAccess: NotRequired[bool]
    """Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution."""

class enableParameters(TypedDict, total=False):
    enableFileChooserOpenedEvent: NotRequired[bool]
    """If true, the Page.fileChooserOpened event will be emitted regardless of the state set by Page.setInterceptFileChooserDialog command (default: false)."""
class getAppManifestParameters(TypedDict, total=False):
    manifestId: NotRequired[str]


class getAdScriptAncestryParameters(TypedDict, total=True):
    frameId: FrameId




class getResourceContentParameters(TypedDict, total=True):
    frameId: FrameId
    """Frame id to get resource for."""
    url: str
    """URL of the resource to get content for."""

class handleJavaScriptDialogParameters(TypedDict, total=True):
    accept: bool
    """Whether to accept or dismiss the dialog."""
    promptText: NotRequired[str]
    """The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog."""
class navigateParameters(TypedDict, total=True):
    url: str
    """URL to navigate the page to."""
    referrer: NotRequired[str]
    """Referrer URL."""
    transitionType: NotRequired[TransitionType]
    """Intended transition type."""
    frameId: NotRequired[FrameId]
    """Frame id to navigate, if not specified navigates the top frame."""
    referrerPolicy: NotRequired[ReferrerPolicy]
    """Referrer-policy used for the navigation."""
class navigateToHistoryEntryParameters(TypedDict, total=True):
    entryId: int
    """Unique id of the entry to navigate to."""
class printToPDFParameters(TypedDict, total=False):
    landscape: NotRequired[bool]
    """Paper orientation. Defaults to false."""
    displayHeaderFooter: NotRequired[bool]
    """Display header and footer. Defaults to false."""
    printBackground: NotRequired[bool]
    """Print background graphics. Defaults to false."""
    scale: NotRequired[float]
    """Scale of the webpage rendering. Defaults to 1."""
    paperWidth: NotRequired[float]
    """Paper width in inches. Defaults to 8.5 inches."""
    paperHeight: NotRequired[float]
    """Paper height in inches. Defaults to 11 inches."""
    marginTop: NotRequired[float]
    """Top margin in inches. Defaults to 1cm (~0.4 inches)."""
    marginBottom: NotRequired[float]
    """Bottom margin in inches. Defaults to 1cm (~0.4 inches)."""
    marginLeft: NotRequired[float]
    """Left margin in inches. Defaults to 1cm (~0.4 inches)."""
    marginRight: NotRequired[float]
    """Right margin in inches. Defaults to 1cm (~0.4 inches)."""
    pageRanges: NotRequired[str]
    """Paper ranges to print, one based, e.g., '1-5, 8, 11-13'. Pages are printed in the document order, not in the order specified, and no more than once. Defaults to empty string, which implies the entire document is printed. The page numbers are quietly capped to actual page count of the document, and ranges beyond the end of the document are ignored. If this results in no pages to print, an error is reported. It is an error to specify a range with start greater than end."""
    headerTemplate: NotRequired[str]
    """HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - date: formatted print date - title: document title - url: document location - pageNumber: current page number - totalPages: total pages in the document  For example, <span class=title></span> would generate span containing the title."""
    footerTemplate: NotRequired[str]
    """HTML template for the print footer. Should use the same format as the headerTemplate."""
    preferCSSPageSize: NotRequired[bool]
    """Whether or not to prefer page size as defined by css. Defaults to false, in which case the content will be scaled to fit the paper size."""
    transferMode: NotRequired[Literal["ReturnAsBase64", "ReturnAsStream"]]
    """return as stream"""
    generateTaggedPDF: NotRequired[bool]
    """Whether or not to generate tagged (accessible) PDF. Defaults to embedder choice."""
    generateDocumentOutline: NotRequired[bool]
    """Whether or not to embed the document outline into the PDF."""
class reloadParameters(TypedDict, total=False):
    ignoreCache: NotRequired[bool]
    """If true, browser cache is ignored (as if the user pressed Shift+refresh)."""
    scriptToEvaluateOnLoad: NotRequired[str]
    """If set, the script will be injected into all frames of the inspected page after reload. Argument will be ignored if reloading dataURL origin."""
    loaderId: NotRequired[LoaderId]
    """If set, an error will be thrown if the target page's main frame's loader id does not match the provided id. This prevents accidentally reloading an unintended target in case there's a racing navigation."""
class removeScriptToEvaluateOnNewDocumentParameters(TypedDict, total=True):
    identifier: ScriptIdentifier
class screencastFrameAckParameters(TypedDict, total=True):
    sessionId: int
    """Frame number."""
class searchInResourceParameters(TypedDict, total=True):
    frameId: FrameId
    """Frame id for resource to search in."""
    url: str
    """URL of the resource to search in."""
    query: str
    """String to search for."""
    caseSensitive: NotRequired[bool]
    """If true, search is case sensitive."""
    isRegex: NotRequired[bool]
    """If true, treats string parameter as regex."""
class setAdBlockingEnabledParameters(TypedDict, total=True):
    enabled: bool
    """Whether to block ads."""
class setBypassCSPParameters(TypedDict, total=True):
    enabled: bool
    """Whether to bypass page CSP."""
class getPermissionsPolicyStateParameters(TypedDict, total=True):
    frameId: FrameId
class getOriginTrialsParameters(TypedDict, total=True):
    frameId: FrameId
class setFontFamiliesParameters(TypedDict, total=True):
    fontFamilies: FontFamilies
    """Specifies font families to set. If a font family is not specified, it won't be changed."""
    forScripts: NotRequired[List[ScriptFontFamilies]]
    """Specifies font families to set for individual scripts."""
class setFontSizesParameters(TypedDict, total=True):
    fontSizes: FontSizes
    """Specifies font sizes to set. If a font size is not specified, it won't be changed."""
class setDocumentContentParameters(TypedDict, total=True):
    frameId: FrameId
    """Frame id to set HTML for."""
    html: str
    """HTML content to set."""
class setLifecycleEventsEnabledParameters(TypedDict, total=True):
    enabled: bool
    """If true, starts emitting lifecycle events."""
class startScreencastParameters(TypedDict, total=False):
    format: NotRequired[Literal["jpeg", "png"]]
    """Image compression format."""
    quality: NotRequired[int]
    """Compression quality from range [0..100]."""
    maxWidth: NotRequired[int]
    """Maximum screenshot width."""
    maxHeight: NotRequired[int]
    """Maximum screenshot height."""
    everyNthFrame: NotRequired[int]
    """Send every n-th frame."""



class setWebLifecycleStateParameters(TypedDict, total=True):
    state: Literal["frozen", "active"]
    """Target lifecycle state"""

class produceCompilationCacheParameters(TypedDict, total=True):
    scripts: List[CompilationCacheParams]
class addCompilationCacheParameters(TypedDict, total=True):
    url: str
    data: str
    """Base64-encoded data (Encoded as a base64 string when passed over JSON)"""

class setSPCTransactionModeParameters(TypedDict, total=True):
    mode: Literal["none", "autoAccept", "autoChooseToAuthAnotherWay", "autoReject", "autoOptOut"]
class setRPHRegistrationModeParameters(TypedDict, total=True):
    mode: Literal["none", "autoAccept", "autoReject"]
class generateTestReportParameters(TypedDict, total=True):
    message: str
    """Message to be displayed in the report."""
    group: NotRequired[str]
    """Specifies the endpoint group to deliver the report to."""

class setInterceptFileChooserDialogParameters(TypedDict, total=True):
    enabled: bool
    cancel: NotRequired[bool]
    """If true, cancels the dialog by emitting relevant events (if any) in addition to not showing it if the interception is enabled (default: false)."""
class setPrerenderingAllowedParameters(TypedDict, total=True):
    isAllowed: bool
class getAnnotatedPageContentParameters(TypedDict, total=False):
    includeActionableInformation: NotRequired[bool]
    """Whether to include actionable information. Defaults to true."""
class addScriptToEvaluateOnNewDocumentReturns(TypedDict):
    identifier: ScriptIdentifier
    """Identifier of the added script."""

class captureScreenshotReturns(TypedDict):
    data: str
    """Base64-encoded image data. (Encoded as a base64 string when passed over JSON)"""
class captureSnapshotReturns(TypedDict):
    data: str
    """Serialized page data."""
class createIsolatedWorldReturns(TypedDict):
    executionContextId: ExecutionContextId
    """Execution context of the isolated world."""


class getAppManifestReturns(TypedDict):
    url: str
    """Manifest location."""
    errors: List[AppManifestError]
    data: str
    """Manifest content."""
    parsed: AppManifestParsedProperties
    """Parsed manifest properties. Deprecated, use manifest instead."""
    manifest: WebAppManifest
class getInstallabilityErrorsReturns(TypedDict):
    installabilityErrors: List[InstallabilityError]
class getAppIdReturns(TypedDict):
    appId: str
    """App id, either from manifest's id attribute or computed from start_url"""
    recommendedId: str
    """Recommendation for manifest's id attribute to match current id computed from start_url"""
class getAdScriptAncestryReturns(TypedDict):
    adScriptAncestry: AdScriptAncestry
    """The ancestry chain of ad script identifiers leading to this frame's creation, along with the root script's filterlist rule. The ancestry chain is ordered from the most immediate script (in the frame creation stack) to more distant ancestors (that created the immediately preceding script). Only sent if frame is labelled as an ad and ids are available."""
class getFrameTreeReturns(TypedDict):
    frameTree: FrameTree
    """Present frame tree structure."""
class getLayoutMetricsReturns(TypedDict):
    layoutViewport: LayoutViewport
    """Deprecated metrics relating to the layout viewport. Is in device pixels. Use cssLayoutViewport instead."""
    visualViewport: VisualViewport
    """Deprecated metrics relating to the visual viewport. Is in device pixels. Use cssVisualViewport instead."""
    contentSize: Rect
    """Deprecated size of scrollable area. Is in DP. Use cssContentSize instead."""
    cssLayoutViewport: LayoutViewport
    """Metrics relating to the layout viewport in CSS pixels."""
    cssVisualViewport: VisualViewport
    """Metrics relating to the visual viewport in CSS pixels."""
    cssContentSize: Rect
    """Size of scrollable area in CSS pixels."""
class getNavigationHistoryReturns(TypedDict):
    currentIndex: int
    """Index of the current navigation history entry."""
    entries: List[NavigationEntry]
    """Array of navigation history entries."""

class getResourceContentReturns(TypedDict):
    content: str
    """Resource content."""
    base64Encoded: bool
    """True, if content was served as base64."""
class getResourceTreeReturns(TypedDict):
    frameTree: FrameResourceTree
    """Present frame / resource tree structure."""

class navigateReturns(TypedDict):
    frameId: FrameId
    """Frame id that has navigated (or failed to navigate)"""
    loaderId: LoaderId
    """Loader identifier. This is omitted in case of same-document navigation, as the previously committed loaderId would not change."""
    errorText: str
    """User friendly error message, present if and only if navigation has failed."""
    isDownload: bool
    """Whether the navigation resulted in a download."""

class printToPDFReturns(TypedDict):
    data: str
    """Base64-encoded pdf data. Empty if |returnAsStream| is specified. (Encoded as a base64 string when passed over JSON)"""
    stream: StreamHandle
    """A handle of the stream that holds resulting PDF data."""



class searchInResourceReturns(TypedDict):
    result: List[SearchMatch]
    """List of search matches."""


class getPermissionsPolicyStateReturns(TypedDict):
    states: List[PermissionsPolicyFeatureState]
class getOriginTrialsReturns(TypedDict):
    originTrials: List[OriginTrial]



















class getAnnotatedPageContentReturns(TypedDict):
    content: str
    """The annotated page content as a base64 encoded protobuf. The format is defined by the AnnotatedPageContent message in components/optimization_guide/proto/features/common_quality_data.proto (Encoded as a base64 string when passed over JSON)"""