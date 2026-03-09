"""CDP Network Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import AssociatedCookie
    from cdp.protocol.network.types import BlockedReason
    from cdp.protocol.network.types import BlockedSetCookieWithReason
    from cdp.protocol.network.types import ChallengeEventDetails
    from cdp.protocol.network.types import ClientSecurityState
    from cdp.protocol.network.types import ConnectTiming
    from cdp.protocol.network.types import CookiePartitionKey
    from cdp.protocol.network.types import CorsErrorStatus
    from cdp.protocol.network.types import CreationEventDetails
    from cdp.protocol.network.types import DeviceBoundSession
    from cdp.protocol.network.types import DeviceBoundSessionEventId
    from cdp.protocol.network.types import DeviceBoundSessionWithUsage
    from cdp.protocol.network.types import DirectTCPSocketOptions
    from cdp.protocol.network.types import DirectUDPMessage
    from cdp.protocol.network.types import DirectUDPSocketOptions
    from cdp.protocol.network.types import ExemptedSetCookieWithReason
    from cdp.protocol.network.types import Headers
    from cdp.protocol.network.types import IPAddressSpace
    from cdp.protocol.network.types import Initiator
    from cdp.protocol.network.types import LoaderId
    from cdp.protocol.network.types import MonotonicTime
    from cdp.protocol.network.types import RefreshEventDetails
    from cdp.protocol.network.types import RenderBlockingBehavior
    from cdp.protocol.network.types import ReportingApiEndpoint
    from cdp.protocol.network.types import ReportingApiReport
    from cdp.protocol.network.types import Request
    from cdp.protocol.network.types import RequestId
    from cdp.protocol.network.types import ResourcePriority
    from cdp.protocol.network.types import ResourceType
    from cdp.protocol.network.types import Response
    from cdp.protocol.network.types import SignedExchangeInfo
    from cdp.protocol.network.types import TerminationEventDetails
    from cdp.protocol.network.types import TimeSinceEpoch
    from cdp.protocol.network.types import TrustTokenOperationType
    from cdp.protocol.network.types import WebSocketFrame
    from cdp.protocol.network.types import WebSocketRequest
    from cdp.protocol.network.types import WebSocketResponse
    from cdp.protocol.page.types import FrameId

class dataReceivedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    dataLength: int
    """Data chunk length."""
    encodedDataLength: int
    """Actual bytes received (might be less than dataLength for compressed encodings)."""
    data: NotRequired[str]
    """Data that was received. (Encoded as a base64 string when passed over JSON)"""
class eventSourceMessageReceivedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    eventName: str
    """Message type."""
    eventId: str
    """Message identifier."""
    data: str
    """Message content."""
class loadingFailedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    type: ResourceType
    """Resource type."""
    errorText: str
    """Error message. List of network errors: https://cs.chromium.org/chromium/src/net/base/net_error_list.h"""
    canceled: NotRequired[bool]
    """True if loading was canceled."""
    blockedReason: NotRequired[BlockedReason]
    """The reason why loading was blocked, if any."""
    corsErrorStatus: NotRequired[CorsErrorStatus]
    """The reason why loading was blocked by CORS, if any."""
class loadingFinishedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    encodedDataLength: float
    """Total number of bytes received for this request."""
class requestServedFromCacheEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
class requestWillBeSentEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    loaderId: LoaderId
    """Loader identifier. Empty string if the request is fetched from worker."""
    documentURL: str
    """URL of the document this request is loaded for."""
    request: Request
    """Request data."""
    timestamp: MonotonicTime
    """Timestamp."""
    wallTime: TimeSinceEpoch
    """Timestamp."""
    initiator: Initiator
    """Request initiator."""
    redirectHasExtraInfo: bool
    """In the case that redirectResponse is populated, this flag indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted for the request which was just redirected."""
    redirectResponse: NotRequired[Response]
    """Redirect response data."""
    type: NotRequired[ResourceType]
    """Type of this resource."""
    frameId: NotRequired[FrameId]
    """Frame identifier."""
    hasUserGesture: NotRequired[bool]
    """Whether the request is initiated by a user gesture. Defaults to false."""
    renderBlockingBehavior: NotRequired[RenderBlockingBehavior]
    """The render-blocking behavior of the request."""
class resourceChangedPriorityEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    newPriority: ResourcePriority
    """New priority"""
    timestamp: MonotonicTime
    """Timestamp."""
class signedExchangeReceivedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    info: SignedExchangeInfo
    """Information about the signed exchange response."""
class responseReceivedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    loaderId: LoaderId
    """Loader identifier. Empty string if the request is fetched from worker."""
    timestamp: MonotonicTime
    """Timestamp."""
    type: ResourceType
    """Resource type."""
    response: Response
    """Response data."""
    hasExtraInfo: bool
    """Indicates whether requestWillBeSentExtraInfo and responseReceivedExtraInfo events will be or were emitted for this request."""
    frameId: NotRequired[FrameId]
    """Frame identifier."""
class webSocketClosedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
class webSocketCreatedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    url: str
    """WebSocket request URL."""
    initiator: NotRequired[Initiator]
    """Request initiator."""
class webSocketFrameErrorEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    errorMessage: str
    """WebSocket error message."""
class webSocketFrameReceivedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    response: WebSocketFrame
    """WebSocket response data."""
class webSocketFrameSentEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    response: WebSocketFrame
    """WebSocket response data."""
class webSocketHandshakeResponseReceivedEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    response: WebSocketResponse
    """WebSocket response data."""
class webSocketWillSendHandshakeRequestEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
    wallTime: TimeSinceEpoch
    """UTC Timestamp."""
    request: WebSocketRequest
    """WebSocket request data."""
class webTransportCreatedEvent(TypedDict, total=True):
    transportId: RequestId
    """WebTransport identifier."""
    url: str
    """WebTransport request URL."""
    timestamp: MonotonicTime
    """Timestamp."""
    initiator: NotRequired[Initiator]
    """Request initiator."""
class webTransportConnectionEstablishedEvent(TypedDict, total=True):
    transportId: RequestId
    """WebTransport identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
class webTransportClosedEvent(TypedDict, total=True):
    transportId: RequestId
    """WebTransport identifier."""
    timestamp: MonotonicTime
    """Timestamp."""
class directTCPSocketCreatedEvent(TypedDict, total=True):
    identifier: RequestId
    remoteAddr: str
    remotePort: int
    """Unsigned int 16."""
    options: DirectTCPSocketOptions
    timestamp: MonotonicTime
    initiator: NotRequired[Initiator]
class directTCPSocketOpenedEvent(TypedDict, total=True):
    identifier: RequestId
    remoteAddr: str
    remotePort: int
    """Expected to be unsigned integer."""
    timestamp: MonotonicTime
    localAddr: NotRequired[str]
    localPort: NotRequired[int]
    """Expected to be unsigned integer."""
class directTCPSocketAbortedEvent(TypedDict, total=True):
    identifier: RequestId
    errorMessage: str
    timestamp: MonotonicTime
class directTCPSocketClosedEvent(TypedDict, total=True):
    identifier: RequestId
    timestamp: MonotonicTime
class directTCPSocketChunkSentEvent(TypedDict, total=True):
    identifier: RequestId
    data: str
    timestamp: MonotonicTime
class directTCPSocketChunkReceivedEvent(TypedDict, total=True):
    identifier: RequestId
    data: str
    timestamp: MonotonicTime
class directUDPSocketJoinedMulticastGroupEvent(TypedDict, total=True):
    identifier: RequestId
    IPAddress: str
class directUDPSocketLeftMulticastGroupEvent(TypedDict, total=True):
    identifier: RequestId
    IPAddress: str
class directUDPSocketCreatedEvent(TypedDict, total=True):
    identifier: RequestId
    options: DirectUDPSocketOptions
    timestamp: MonotonicTime
    initiator: NotRequired[Initiator]
class directUDPSocketOpenedEvent(TypedDict, total=True):
    identifier: RequestId
    localAddr: str
    localPort: int
    """Expected to be unsigned integer."""
    timestamp: MonotonicTime
    remoteAddr: NotRequired[str]
    remotePort: NotRequired[int]
    """Expected to be unsigned integer."""
class directUDPSocketAbortedEvent(TypedDict, total=True):
    identifier: RequestId
    errorMessage: str
    timestamp: MonotonicTime
class directUDPSocketClosedEvent(TypedDict, total=True):
    identifier: RequestId
    timestamp: MonotonicTime
class directUDPSocketChunkSentEvent(TypedDict, total=True):
    identifier: RequestId
    message: DirectUDPMessage
    timestamp: MonotonicTime
class directUDPSocketChunkReceivedEvent(TypedDict, total=True):
    identifier: RequestId
    message: DirectUDPMessage
    timestamp: MonotonicTime
class requestWillBeSentExtraInfoEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier. Used to match this information to an existing requestWillBeSent event."""
    associatedCookies: List[AssociatedCookie]
    """A list of cookies potentially associated to the requested URL. This includes both cookies sent with the request and the ones not sent; the latter are distinguished by having blockedReasons field set."""
    headers: Headers
    """Raw request headers as they will be sent over the wire."""
    connectTiming: ConnectTiming
    """Connection timing information for the request."""
    deviceBoundSessionUsages: NotRequired[List[DeviceBoundSessionWithUsage]]
    """How the request site's device bound sessions were used during this request."""
    clientSecurityState: NotRequired[ClientSecurityState]
    """The client security state set for the request."""
    siteHasCookieInOtherPartition: NotRequired[bool]
    """Whether the site has partitioned cookies stored in a partition different than the current one."""
    appliedNetworkConditionsId: NotRequired[str]
    """The network conditions id if this request was affected by network conditions configured via emulateNetworkConditionsByRule."""
class responseReceivedExtraInfoEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier. Used to match this information to another responseReceived event."""
    blockedCookies: List[BlockedSetCookieWithReason]
    """A list of cookies which were not stored from the response along with the corresponding reasons for blocking. The cookies here may not be valid due to syntax errors, which are represented by the invalid cookie line string instead of a proper cookie."""
    headers: Headers
    """Raw response headers as they were received over the wire. Duplicate headers in the response are represented as a single key with their values concatentated using \n as the separator. See also headersText that contains verbatim text for HTTP/1.*."""
    resourceIPAddressSpace: IPAddressSpace
    """The IP address space of the resource. The address space can only be determined once the transport established the connection, so we can't send it in requestWillBeSentExtraInfo."""
    statusCode: int
    """The status code of the response. This is useful in cases the request failed and no responseReceived event is triggered, which is the case for, e.g., CORS errors. This is also the correct status code for cached requests, where the status in responseReceived is a 200 and this will be 304."""
    headersText: NotRequired[str]
    """Raw response header text as it was received over the wire. The raw text may not always be available, such as in the case of HTTP/2 or QUIC."""
    cookiePartitionKey: NotRequired[CookiePartitionKey]
    """The cookie partition key that will be used to store partitioned cookies set in this response. Only sent when partitioned cookies are enabled."""
    cookiePartitionKeyOpaque: NotRequired[bool]
    """True if partitioned cookies are enabled, but the partition key is not serializable to string."""
    exemptedCookies: NotRequired[List[ExemptedSetCookieWithReason]]
    """A list of cookies which should have been blocked by 3PCD but are exempted and stored from the response with the corresponding reason."""
class responseReceivedEarlyHintsEvent(TypedDict, total=True):
    requestId: RequestId
    """Request identifier. Used to match this information to another responseReceived event."""
    headers: Headers
    """Raw response headers as they were received over the wire. Duplicate headers in the response are represented as a single key with their values concatentated using \n as the separator. See also headersText that contains verbatim text for HTTP/1.*."""
class trustTokenOperationDoneEvent(TypedDict, total=True):
    status: Literal["Ok", "InvalidArgument", "MissingIssuerKeys", "FailedPrecondition", "ResourceExhausted", "AlreadyExists", "ResourceLimited", "Unauthorized", "BadResponse", "InternalError", "UnknownError", "FulfilledLocally", "SiteIssuerLimit"]
    """Detailed success or error status of the operation. 'AlreadyExists' also signifies a successful operation, as the result of the operation already exists und thus, the operation was abort preemptively (e.g. a cache hit)."""
    type: TrustTokenOperationType
    requestId: RequestId
    topLevelOrigin: NotRequired[str]
    """Top level origin. The context in which the operation was attempted."""
    issuerOrigin: NotRequired[str]
    """Origin of the issuer in case of a "Issuance" or "Redemption" operation."""
    issuedTokenCount: NotRequired[int]
    """The number of obtained Trust Tokens on a successful "Issuance" operation."""
class policyUpdatedEvent(TypedDict, total=True):
    pass
class reportingApiReportAddedEvent(TypedDict, total=True):
    report: ReportingApiReport
class reportingApiReportUpdatedEvent(TypedDict, total=True):
    report: ReportingApiReport
class reportingApiEndpointsChangedForOriginEvent(TypedDict, total=True):
    origin: str
    """Origin of the document(s) which configured the endpoints."""
    endpoints: List[ReportingApiEndpoint]
class deviceBoundSessionsAddedEvent(TypedDict, total=True):
    sessions: List[DeviceBoundSession]
    """The device bound sessions."""
class deviceBoundSessionEventOccurredEvent(TypedDict, total=True):
    eventId: DeviceBoundSessionEventId
    """A unique identifier for this session event."""
    site: str
    """The site this session event is associated with."""
    succeeded: bool
    """Whether this event was considered successful."""
    sessionId: NotRequired[str]
    """The session ID this event is associated with. May not be populated for failed events."""
    creationEventDetails: NotRequired[CreationEventDetails]
    """The below are the different session event type details. Exactly one is populated."""
    refreshEventDetails: NotRequired[RefreshEventDetails]
    terminationEventDetails: NotRequired[TerminationEventDetails]
    challengeEventDetails: NotRequired[ChallengeEventDetails]