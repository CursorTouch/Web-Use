"""CDP Network Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.io.types import StreamHandle
    from cdp.protocol.runtime.types import StackTrace
    from cdp.protocol.security.types import CertificateId
    from cdp.protocol.security.types import MixedContentType
    from cdp.protocol.security.types import SecurityState

ResourceType = Literal['Document','Stylesheet','Image','Media','Font','Script','TextTrack','XHR','Fetch','Prefetch','EventSource','WebSocket','Manifest','SignedExchange','Ping','CSPViolationReport','Preflight','FedCM','Other']
"""Resource type as it was perceived by the rendering engine."""
LoaderId = str
"""Unique loader identifier."""
RequestId = str
"""Unique network request identifier. Note that this does not identify individual HTTP requests that are part of a network request."""
InterceptionId = str
"""Unique intercepted request identifier."""
ErrorReason = Literal['Failed','Aborted','TimedOut','AccessDenied','ConnectionClosed','ConnectionReset','ConnectionRefused','ConnectionAborted','ConnectionFailed','NameNotResolved','InternetDisconnected','AddressUnreachable','BlockedByClient','BlockedByResponse']
"""Network level fetch failure reason."""
TimeSinceEpoch = float
"""UTC time in seconds, counted from January 1, 1970."""
MonotonicTime = float
"""Monotonically increasing time in seconds since an arbitrary point in the past."""
class Headers(TypedDict, total=True):
    """Request / response headers as keys / values of JSON object."""
    pass
ConnectionType = Literal['none','cellular2g','cellular3g','cellular4g','bluetooth','ethernet','wifi','wimax','other']
"""The underlying connection technology that the browser is supposedly using."""
CookieSameSite = Literal['Strict','Lax','None']
"""Represents the cookie's 'SameSite' status: https://tools.ietf.org/html/draft-west-first-party-cookies"""
CookiePriority = Literal['Low','Medium','High']
"""Represents the cookie's 'Priority' status: https://tools.ietf.org/html/draft-west-cookie-priority-00"""
CookieSourceScheme = Literal['Unset','NonSecure','Secure']
"""Represents the source scheme of the origin that originally set the cookie. A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme. This is a temporary ability and it will be removed in the future."""
class ResourceTiming(TypedDict, total=True):
    """Timing information for the request."""
    requestTime: float
    """Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime."""
    proxyStart: float
    """Started resolving proxy."""
    proxyEnd: float
    """Finished resolving proxy."""
    dnsStart: float
    """Started DNS address resolve."""
    dnsEnd: float
    """Finished DNS address resolve."""
    connectStart: float
    """Started connecting to the remote host."""
    connectEnd: float
    """Connected to the remote host."""
    sslStart: float
    """Started SSL handshake."""
    sslEnd: float
    """Finished SSL handshake."""
    workerStart: float
    """Started running ServiceWorker."""
    workerReady: float
    """Finished Starting ServiceWorker."""
    workerFetchStart: float
    """Started fetch event."""
    workerRespondWithSettled: float
    """Settled fetch event respondWith promise."""
    sendStart: float
    """Started sending request."""
    sendEnd: float
    """Finished sending request."""
    pushStart: float
    """Time the server started pushing request."""
    pushEnd: float
    """Time the server finished pushing request."""
    receiveHeadersStart: float
    """Started receiving response headers."""
    receiveHeadersEnd: float
    """Finished receiving response headers."""
    workerRouterEvaluationStart: NotRequired[float]
    """Started ServiceWorker static routing source evaluation."""
    workerCacheLookupStart: NotRequired[float]
    """Started cache lookup when the source was evaluated to cache."""
ResourcePriority = Literal['VeryLow','Low','Medium','High','VeryHigh']
"""Loading priority of a resource request."""
RenderBlockingBehavior = Literal['Blocking','InBodyParserBlocking','NonBlocking','NonBlockingDynamic','PotentiallyBlocking']
"""The render-blocking behavior of a resource request."""
class PostDataEntry(TypedDict, total=False):
    """Post data entry for HTTP request"""
    bytes: NotRequired[str]
class Request(TypedDict, total=True):
    """HTTP request data."""
    url: str
    """Request URL (without fragment)."""
    method: str
    """HTTP request method."""
    headers: Headers
    """HTTP request headers."""
    initialPriority: ResourcePriority
    """Priority of the resource request at the time request is sent."""
    referrerPolicy: Literal["unsafe-url", "no-referrer-when-downgrade", "no-referrer", "origin", "origin-when-cross-origin", "same-origin", "strict-origin", "strict-origin-when-cross-origin"]
    """The referrer policy of the request, as defined in https://www.w3.org/TR/referrer-policy/"""
    urlFragment: NotRequired[str]
    """Fragment of the requested URL starting with hash, if present."""
    hasPostData: NotRequired[bool]
    """True when the request has POST data. Note that postData might still be omitted when this flag is true when the data is too long."""
    postDataEntries: NotRequired[List[PostDataEntry]]
    """Request body elements (post data broken into individual entries)."""
    mixedContentType: NotRequired[MixedContentType]
    """The mixed content type of the request."""
    isLinkPreload: NotRequired[bool]
    """Whether is loaded via link preload."""
    trustTokenParams: NotRequired[TrustTokenParams]
    """Set for requests when the TrustToken API is used. Contains the parameters passed by the developer (e.g. via "fetch") as understood by the backend."""
    isSameSite: NotRequired[bool]
    """True if this resource request is considered to be the 'same site' as the request corresponding to the main frame."""
    isAdRelated: NotRequired[bool]
    """True when the resource request is ad-related."""
class SignedCertificateTimestamp(TypedDict, total=True):
    """Details of a signed certificate timestamp (SCT)."""
    status: str
    """Validation status."""
    origin: str
    """Origin."""
    logDescription: str
    """Log name / description."""
    logId: str
    """Log ID."""
    timestamp: float
    """Issuance date. Unlike TimeSinceEpoch, this contains the number of milliseconds since January 1, 1970, UTC, not the number of seconds."""
    hashAlgorithm: str
    """Hash algorithm."""
    signatureAlgorithm: str
    """Signature algorithm."""
    signatureData: str
    """Signature data."""
class SecurityDetails(TypedDict, total=True):
    """Security details about a request."""
    protocol: str
    """Protocol name (e.g. TLS 1.2 or QUIC)."""
    keyExchange: str
    """Key Exchange used by the connection, or the empty string if not applicable."""
    cipher: str
    """Cipher name."""
    certificateId: CertificateId
    """Certificate ID value."""
    subjectName: str
    """Certificate subject name."""
    sanList: List[str]
    """Subject Alternative Name (SAN) DNS names and IP addresses."""
    issuer: str
    """Name of the issuing CA."""
    validFrom: TimeSinceEpoch
    """Certificate valid from date."""
    validTo: TimeSinceEpoch
    """Certificate valid to (expiration) date"""
    signedCertificateTimestampList: List[SignedCertificateTimestamp]
    """List of signed certificate timestamps (SCTs)."""
    certificateTransparencyCompliance: CertificateTransparencyCompliance
    """Whether the request complied with Certificate Transparency policy"""
    encryptedClientHello: bool
    """Whether the connection used Encrypted ClientHello"""
    keyExchangeGroup: NotRequired[str]
    """(EC)DH group used by the connection, if applicable."""
    mac: NotRequired[str]
    """TLS MAC. Note that AEAD ciphers do not have separate MACs."""
    serverSignatureAlgorithm: NotRequired[int]
    """The signature algorithm used by the server in the TLS server signature, represented as a TLS SignatureScheme code point. Omitted if not applicable or not known."""
CertificateTransparencyCompliance = Literal['unknown','not-compliant','compliant']
"""Whether the request complied with Certificate Transparency policy."""
BlockedReason = Literal['other','csp','mixed-content','origin','inspector','integrity','subresource-filter','content-type','coep-frame-resource-needs-coep-header','coop-sandboxed-iframe-cannot-navigate-to-coop-page','corp-not-same-origin','corp-not-same-origin-after-defaulted-to-same-origin-by-coep','corp-not-same-origin-after-defaulted-to-same-origin-by-dip','corp-not-same-origin-after-defaulted-to-same-origin-by-coep-and-dip','corp-not-same-site','sri-message-signature-mismatch']
"""The reason why request was blocked."""
CorsError = Literal['DisallowedByMode','InvalidResponse','WildcardOriginNotAllowed','MissingAllowOriginHeader','MultipleAllowOriginValues','InvalidAllowOriginValue','AllowOriginMismatch','InvalidAllowCredentials','CorsDisabledScheme','PreflightInvalidStatus','PreflightDisallowedRedirect','PreflightWildcardOriginNotAllowed','PreflightMissingAllowOriginHeader','PreflightMultipleAllowOriginValues','PreflightInvalidAllowOriginValue','PreflightAllowOriginMismatch','PreflightInvalidAllowCredentials','PreflightMissingAllowExternal','PreflightInvalidAllowExternal','InvalidAllowMethodsPreflightResponse','InvalidAllowHeadersPreflightResponse','MethodDisallowedByPreflightResponse','HeaderDisallowedByPreflightResponse','RedirectContainsCredentials','InsecureLocalNetwork','InvalidLocalNetworkAccess','NoCorsRedirectModeNotFollow','LocalNetworkAccessPermissionDenied']
"""The reason why request was blocked."""
class CorsErrorStatus(TypedDict, total=True):
    corsError: CorsError
    failedParameter: str
ServiceWorkerResponseSource = Literal['cache-storage','http-cache','fallback-code','network']
"""Source of serviceworker response."""
class TrustTokenParams(TypedDict, total=True):
    """Determines what type of Trust Token operation is executed and depending on the type, some additional parameters. The values are specified in third_party/blink/renderer/core/fetch/trust_token.idl."""
    operation: TrustTokenOperationType
    refreshPolicy: Literal["UseCached", "Refresh"]
    """Only set for token-redemption operation and determine whether to request a fresh SRR or use a still valid cached SRR."""
    issuers: NotRequired[List[str]]
    """Origins of issuers from whom to request tokens or redemption records."""
TrustTokenOperationType = Literal['Issuance','Redemption','Signing']
AlternateProtocolUsage = Literal['alternativeJobWonWithoutRace','alternativeJobWonRace','mainJobWonRace','mappingMissing','broken','dnsAlpnH3JobWonWithoutRace','dnsAlpnH3JobWonRace','unspecifiedReason']
"""The reason why Chrome uses a specific transport protocol for HTTP semantics."""
ServiceWorkerRouterSource = Literal['network','cache','fetch-event','race-network-and-fetch-handler','race-network-and-cache']
"""Source of service worker router."""
class ServiceWorkerRouterInfo(TypedDict, total=False):
    ruleIdMatched: NotRequired[int]
    """ID of the rule matched. If there is a matched rule, this field will be set, otherwiser no value will be set."""
    matchedSourceType: NotRequired[ServiceWorkerRouterSource]
    """The router source of the matched rule. If there is a matched rule, this field will be set, otherwise no value will be set."""
    actualSourceType: NotRequired[ServiceWorkerRouterSource]
    """The actual router source used."""
class Response(TypedDict, total=True):
    """HTTP response data."""
    url: str
    """Response URL. This URL can be different from CachedResource.url in case of redirect."""
    status: int
    """HTTP response status code."""
    statusText: str
    """HTTP response status text."""
    headers: Headers
    """HTTP response headers."""
    mimeType: str
    """Resource mimeType as determined by the browser."""
    charset: str
    """Resource charset as determined by the browser (if applicable)."""
    connectionReused: bool
    """Specifies whether physical connection was actually reused for this request."""
    connectionId: float
    """Physical connection id that was actually used for this request."""
    encodedDataLength: float
    """Total number of bytes received for this request so far."""
    securityState: SecurityState
    """Security state of the request resource."""
    requestHeaders: NotRequired[Headers]
    """Refined HTTP request headers that were actually transmitted over the network."""
    remoteIPAddress: NotRequired[str]
    """Remote IP address."""
    remotePort: NotRequired[int]
    """Remote port."""
    fromDiskCache: NotRequired[bool]
    """Specifies that the request was served from the disk cache."""
    fromServiceWorker: NotRequired[bool]
    """Specifies that the request was served from the ServiceWorker."""
    fromPrefetchCache: NotRequired[bool]
    """Specifies that the request was served from the prefetch cache."""
    fromEarlyHints: NotRequired[bool]
    """Specifies that the request was served from the prefetch cache."""
    serviceWorkerRouterInfo: NotRequired[ServiceWorkerRouterInfo]
    """Information about how ServiceWorker Static Router API was used. If this field is set with matchedSourceType field, a matching rule is found. If this field is set without matchedSource, no matching rule is found. Otherwise, the API is not used."""
    timing: NotRequired[ResourceTiming]
    """Timing information for the given request."""
    serviceWorkerResponseSource: NotRequired[ServiceWorkerResponseSource]
    """Response source of response from ServiceWorker."""
    responseTime: NotRequired[TimeSinceEpoch]
    """The time at which the returned response was generated."""
    cacheStorageCacheName: NotRequired[str]
    """Cache Storage Cache Name."""
    protocol: NotRequired[str]
    """Protocol used to fetch this request."""
    alternateProtocolUsage: NotRequired[AlternateProtocolUsage]
    """The reason why Chrome uses a specific transport protocol for HTTP semantics."""
    securityDetails: NotRequired[SecurityDetails]
    """Security details for the request."""
class WebSocketRequest(TypedDict, total=True):
    """WebSocket request data."""
    headers: Headers
    """HTTP request headers."""
class WebSocketResponse(TypedDict, total=True):
    """WebSocket response data."""
    status: int
    """HTTP response status code."""
    statusText: str
    """HTTP response status text."""
    headers: Headers
    """HTTP response headers."""
    headersText: NotRequired[str]
    """HTTP response headers text."""
    requestHeaders: NotRequired[Headers]
    """HTTP request headers."""
    requestHeadersText: NotRequired[str]
    """HTTP request headers text."""
class WebSocketFrame(TypedDict, total=True):
    """WebSocket message data. This represents an entire WebSocket message, not just a fragmented frame as the name suggests."""
    opcode: float
    """WebSocket message opcode."""
    mask: bool
    """WebSocket message mask."""
    payloadData: str
    """WebSocket message payload data. If the opcode is 1, this is a text message and payloadData is a UTF-8 string. If the opcode isn't 1, then payloadData is a base64 encoded string representing binary data."""
class CachedResource(TypedDict, total=True):
    """Information about the cached resource."""
    url: str
    """Resource URL. This is the url of the original network request."""
    type: ResourceType
    """Type of this resource."""
    bodySize: float
    """Cached response body size."""
    response: NotRequired[Response]
    """Cached response data."""
class Initiator(TypedDict, total=True):
    """Information about the request initiator."""
    type: Literal["parser", "script", "preload", "SignedExchange", "preflight", "FedCM", "other"]
    """Type of this initiator."""
    stack: NotRequired[StackTrace]
    """Initiator JavaScript stack trace, set for Script only. Requires the Debugger domain to be enabled."""
    url: NotRequired[str]
    """Initiator URL, set for Parser type or for Script type (when script is importing module) or for SignedExchange type."""
    lineNumber: NotRequired[float]
    """Initiator line number, set for Parser type or for Script type (when script is importing module) (0-based)."""
    columnNumber: NotRequired[float]
    """Initiator column number, set for Parser type or for Script type (when script is importing module) (0-based)."""
    requestId: NotRequired[RequestId]
    """Set if another request triggered this request (e.g. preflight)."""
class CookiePartitionKey(TypedDict, total=True):
    """cookiePartitionKey object The representation of the components of the key that are created by the cookiePartitionKey class contained in net/cookies/cookie_partition_key.h."""
    topLevelSite: str
    """The site of the top-level URL the browser was visiting at the start of the request to the endpoint that set the cookie."""
    hasCrossSiteAncestor: bool
    """Indicates if the cookie has any ancestors that are cross-site to the topLevelSite."""
class Cookie(TypedDict, total=True):
    """Cookie object"""
    name: str
    """Cookie name."""
    value: str
    """Cookie value."""
    domain: str
    """Cookie domain."""
    path: str
    """Cookie path."""
    expires: float
    """Cookie expiration date as the number of seconds since the UNIX epoch. The value is set to -1 if the expiry date is not set. The value can be null for values that cannot be represented in JSON (±Inf)."""
    size: int
    """Cookie size."""
    httpOnly: bool
    """True if cookie is http-only."""
    secure: bool
    """True if cookie is secure."""
    session: bool
    """True in case of session cookie."""
    priority: CookiePriority
    """Cookie Priority"""
    sourceScheme: CookieSourceScheme
    """Cookie source scheme type."""
    sourcePort: int
    """Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future."""
    sameSite: NotRequired[CookieSameSite]
    """Cookie SameSite type."""
    partitionKey: NotRequired[CookiePartitionKey]
    """Cookie partition key."""
    partitionKeyOpaque: NotRequired[bool]
    """True if cookie partition key is opaque."""
SetCookieBlockedReason = Literal['SecureOnly','SameSiteStrict','SameSiteLax','SameSiteUnspecifiedTreatedAsLax','SameSiteNoneInsecure','UserPreferences','ThirdPartyPhaseout','ThirdPartyBlockedInFirstPartySet','SyntaxError','SchemeNotSupported','OverwriteSecure','InvalidDomain','InvalidPrefix','UnknownError','SchemefulSameSiteStrict','SchemefulSameSiteLax','SchemefulSameSiteUnspecifiedTreatedAsLax','NameValuePairExceedsMaxSize','DisallowedCharacter','NoCookieContent']
"""Types of reasons why a cookie may not be stored from a response."""
CookieBlockedReason = Literal['SecureOnly','NotOnPath','DomainMismatch','SameSiteStrict','SameSiteLax','SameSiteUnspecifiedTreatedAsLax','SameSiteNoneInsecure','UserPreferences','ThirdPartyPhaseout','ThirdPartyBlockedInFirstPartySet','UnknownError','SchemefulSameSiteStrict','SchemefulSameSiteLax','SchemefulSameSiteUnspecifiedTreatedAsLax','NameValuePairExceedsMaxSize','PortMismatch','SchemeMismatch','AnonymousContext']
"""Types of reasons why a cookie may not be sent with a request."""
CookieExemptionReason = Literal['None','UserSetting','TPCDMetadata','TPCDDeprecationTrial','TopLevelTPCDDeprecationTrial','TPCDHeuristics','EnterprisePolicy','StorageAccess','TopLevelStorageAccess','Scheme','SameSiteNoneCookiesInSandbox']
"""Types of reasons why a cookie should have been blocked by 3PCD but is exempted for the request."""
class BlockedSetCookieWithReason(TypedDict, total=True):
    """A cookie which was not stored from a response with the corresponding reason."""
    blockedReasons: List[SetCookieBlockedReason]
    """The reason(s) this cookie was blocked."""
    cookieLine: str
    """The string representing this individual cookie as it would appear in the header. This is not the entire cookie or set-cookie header which could have multiple cookies."""
    cookie: NotRequired[Cookie]
    """The cookie object which represents the cookie which was not stored. It is optional because sometimes complete cookie information is not available, such as in the case of parsing errors."""
class ExemptedSetCookieWithReason(TypedDict, total=True):
    """A cookie should have been blocked by 3PCD but is exempted and stored from a response with the corresponding reason. A cookie could only have at most one exemption reason."""
    exemptionReason: CookieExemptionReason
    """The reason the cookie was exempted."""
    cookieLine: str
    """The string representing this individual cookie as it would appear in the header."""
    cookie: Cookie
    """The cookie object representing the cookie."""
class AssociatedCookie(TypedDict, total=True):
    """A cookie associated with the request which may or may not be sent with it. Includes the cookies itself and reasons for blocking or exemption."""
    cookie: Cookie
    """The cookie object representing the cookie which was not sent."""
    blockedReasons: List[CookieBlockedReason]
    """The reason(s) the cookie was blocked. If empty means the cookie is included."""
    exemptionReason: NotRequired[CookieExemptionReason]
    """The reason the cookie should have been blocked by 3PCD but is exempted. A cookie could only have at most one exemption reason."""
class CookieParam(TypedDict, total=True):
    """Cookie parameter object"""
    name: str
    """Cookie name."""
    value: str
    """Cookie value."""
    url: NotRequired[str]
    """The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie."""
    domain: NotRequired[str]
    """Cookie domain."""
    path: NotRequired[str]
    """Cookie path."""
    secure: NotRequired[bool]
    """True if cookie is secure."""
    httpOnly: NotRequired[bool]
    """True if cookie is http-only."""
    sameSite: NotRequired[CookieSameSite]
    """Cookie SameSite type."""
    expires: NotRequired[TimeSinceEpoch]
    """Cookie expiration date, session cookie if not set"""
    priority: NotRequired[CookiePriority]
    """Cookie Priority."""
    sourceScheme: NotRequired[CookieSourceScheme]
    """Cookie source scheme type."""
    sourcePort: NotRequired[int]
    """Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port. An unspecified port value allows protocol clients to emulate legacy cookie scope for the port. This is a temporary ability and it will be removed in the future."""
    partitionKey: NotRequired[CookiePartitionKey]
    """Cookie partition key. If not set, the cookie will be set as not partitioned."""
class AuthChallenge(TypedDict, total=True):
    """Authorization challenge for HTTP status code 401 or 407."""
    origin: str
    """Origin of the challenger."""
    scheme: str
    """The authentication scheme used, such as basic or digest"""
    realm: str
    """The realm of the challenge. May be empty."""
    source: NotRequired[Literal["Server", "Proxy"]]
    """Source of the authentication challenge."""
class AuthChallengeResponse(TypedDict, total=True):
    """Response to an AuthChallenge."""
    response: Literal["Default", "CancelAuth", "ProvideCredentials"]
    """The decision on what to do in response to the authorization challenge.  Default means deferring to the default behavior of the net stack, which will likely either the Cancel authentication or display a popup dialog box."""
    username: NotRequired[str]
    """The username to provide, possibly empty. Should only be set if response is ProvideCredentials."""
    password: NotRequired[str]
    """The password to provide, possibly empty. Should only be set if response is ProvideCredentials."""
InterceptionStage = Literal['Request','HeadersReceived']
"""Stages of the interception to begin intercepting. Request will intercept before the request is sent. Response will intercept after the response is received."""
class RequestPattern(TypedDict, total=False):
    """Request pattern for interception."""
    urlPattern: NotRequired[str]
    """Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to "*"."""
    resourceType: NotRequired[ResourceType]
    """If set, only requests for matching resource types will be intercepted."""
    interceptionStage: NotRequired[InterceptionStage]
    """Stage at which to begin intercepting requests. Default is Request."""
class SignedExchangeSignature(TypedDict, total=True):
    """Information about a signed exchange signature. https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#rfc.section.3.1"""
    label: str
    """Signed exchange signature label."""
    signature: str
    """The hex string of signed exchange signature."""
    integrity: str
    """Signed exchange signature integrity."""
    validityUrl: str
    """Signed exchange signature validity Url."""
    date: int
    """Signed exchange signature date."""
    expires: int
    """Signed exchange signature expires."""
    certUrl: NotRequired[str]
    """Signed exchange signature cert Url."""
    certSha256: NotRequired[str]
    """The hex string of signed exchange signature cert sha256."""
    certificates: NotRequired[List[str]]
    """The encoded certificates."""
class SignedExchangeHeader(TypedDict, total=True):
    """Information about a signed exchange header. https://wicg.github.io/webpackage/draft-yasskin-httpbis-origin-signed-exchanges-impl.html#cbor-representation"""
    requestUrl: str
    """Signed exchange request URL."""
    responseCode: int
    """Signed exchange response code."""
    responseHeaders: Headers
    """Signed exchange response headers."""
    signatures: List[SignedExchangeSignature]
    """Signed exchange response signature."""
    headerIntegrity: str
    """Signed exchange header integrity hash in the form of sha256-<base64-hash-value>."""
SignedExchangeErrorField = Literal['signatureSig','signatureIntegrity','signatureCertUrl','signatureCertSha256','signatureValidityUrl','signatureTimestamps']
"""Field type for a signed exchange related error."""
class SignedExchangeError(TypedDict, total=True):
    """Information about a signed exchange response."""
    message: str
    """Error message."""
    signatureIndex: NotRequired[int]
    """The index of the signature which caused the error."""
    errorField: NotRequired[SignedExchangeErrorField]
    """The field which caused the error."""
class SignedExchangeInfo(TypedDict, total=True):
    """Information about a signed exchange response."""
    outerResponse: Response
    """The outer response of signed HTTP exchange which was received from network."""
    hasExtraInfo: bool
    """Whether network response for the signed exchange was accompanied by extra headers."""
    header: NotRequired[SignedExchangeHeader]
    """Information about the signed exchange header."""
    securityDetails: NotRequired[SecurityDetails]
    """Security details for the signed exchange header."""
    errors: NotRequired[List[SignedExchangeError]]
    """Errors occurred while handling the signed exchange."""
ContentEncoding = Literal['deflate','gzip','br','zstd']
"""List of content encodings supported by the backend."""
class NetworkConditions(TypedDict, total=True):
    urlPattern: str
    """Only matching requests will be affected by these conditions. Patterns use the URLPattern constructor string syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. If the pattern is empty, all requests are matched (including p2p connections)."""
    latency: float
    """Minimum latency from request sent to response headers received (ms)."""
    downloadThroughput: float
    """Maximal aggregated download throughput (bytes/sec). -1 disables download throttling."""
    uploadThroughput: float
    """Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling."""
    connectionType: NotRequired[ConnectionType]
    """Connection type if known."""
    packetLoss: NotRequired[float]
    """WebRTC packet loss (percent, 0-100). 0 disables packet loss emulation, 100 drops all the packets."""
    packetQueueLength: NotRequired[int]
    """WebRTC packet queue length (packet). 0 removes any queue length limitations."""
    packetReordering: NotRequired[bool]
    """WebRTC packetReordering feature."""
class BlockPattern(TypedDict, total=True):
    urlPattern: str
    """URL pattern to match. Patterns use the URLPattern constructor string syntax (https://urlpattern.spec.whatwg.org/) and must be absolute. Example: *://*:*/*.css."""
    block: bool
    """Whether or not to block the pattern. If false, a matching request will not be blocked even if it matches a later BlockPattern."""
DirectSocketDnsQueryType = Literal['ipv4','ipv6']
class DirectTCPSocketOptions(TypedDict, total=True):
    noDelay: bool
    """TCP_NODELAY option"""
    keepAliveDelay: NotRequired[float]
    """Expected to be unsigned integer."""
    sendBufferSize: NotRequired[float]
    """Expected to be unsigned integer."""
    receiveBufferSize: NotRequired[float]
    """Expected to be unsigned integer."""
    dnsQueryType: NotRequired[DirectSocketDnsQueryType]
class DirectUDPSocketOptions(TypedDict, total=False):
    remoteAddr: NotRequired[str]
    remotePort: NotRequired[int]
    """Unsigned int 16."""
    localAddr: NotRequired[str]
    localPort: NotRequired[int]
    """Unsigned int 16."""
    dnsQueryType: NotRequired[DirectSocketDnsQueryType]
    sendBufferSize: NotRequired[float]
    """Expected to be unsigned integer."""
    receiveBufferSize: NotRequired[float]
    """Expected to be unsigned integer."""
    multicastLoopback: NotRequired[bool]
    multicastTimeToLive: NotRequired[int]
    """Unsigned int 8."""
    multicastAllowAddressSharing: NotRequired[bool]
class DirectUDPMessage(TypedDict, total=True):
    data: str
    remoteAddr: NotRequired[str]
    """Null for connected mode."""
    remotePort: NotRequired[int]
    """Null for connected mode. Expected to be unsigned integer."""
LocalNetworkAccessRequestPolicy = Literal['Allow','BlockFromInsecureToMorePrivate','WarnFromInsecureToMorePrivate','PermissionBlock','PermissionWarn']
IPAddressSpace = Literal['Loopback','Local','Public','Unknown']
class ConnectTiming(TypedDict, total=True):
    requestTime: float
    """Timing's requestTime is a baseline in seconds, while the other numbers are ticks in milliseconds relatively to this requestTime. Matches ResourceTiming's requestTime for the same request (but not for redirected requests)."""
class ClientSecurityState(TypedDict, total=True):
    initiatorIsSecureContext: bool
    initiatorIPAddressSpace: IPAddressSpace
    localNetworkAccessRequestPolicy: LocalNetworkAccessRequestPolicy
CrossOriginOpenerPolicyValue = Literal['SameOrigin','SameOriginAllowPopups','RestrictProperties','UnsafeNone','SameOriginPlusCoep','RestrictPropertiesPlusCoep','NoopenerAllowPopups']
class CrossOriginOpenerPolicyStatus(TypedDict, total=True):
    value: CrossOriginOpenerPolicyValue
    reportOnlyValue: CrossOriginOpenerPolicyValue
    reportingEndpoint: NotRequired[str]
    reportOnlyReportingEndpoint: NotRequired[str]
CrossOriginEmbedderPolicyValue = Literal['None','Credentialless','RequireCorp']
class CrossOriginEmbedderPolicyStatus(TypedDict, total=True):
    value: CrossOriginEmbedderPolicyValue
    reportOnlyValue: CrossOriginEmbedderPolicyValue
    reportingEndpoint: NotRequired[str]
    reportOnlyReportingEndpoint: NotRequired[str]
ContentSecurityPolicySource = Literal['HTTP','Meta']
class ContentSecurityPolicyStatus(TypedDict, total=True):
    effectiveDirectives: str
    isEnforced: bool
    source: ContentSecurityPolicySource
class SecurityIsolationStatus(TypedDict, total=False):
    coop: NotRequired[CrossOriginOpenerPolicyStatus]
    coep: NotRequired[CrossOriginEmbedderPolicyStatus]
    csp: NotRequired[List[ContentSecurityPolicyStatus]]
ReportStatus = Literal['Queued','Pending','MarkedForRemoval','Success']
"""The status of a Reporting API report."""
ReportId = str
class ReportingApiReport(TypedDict, total=True):
    """An object representing a report generated by the Reporting API."""
    id: ReportId
    initiatorUrl: str
    """The URL of the document that triggered the report."""
    destination: str
    """The name of the endpoint group that should be used to deliver the report."""
    type: str
    """The type of the report (specifies the set of data that is contained in the report body)."""
    timestamp: TimeSinceEpoch
    """When the report was generated."""
    depth: int
    """How many uploads deep the related request was."""
    completedAttempts: int
    """The number of delivery attempts made so far, not including an active attempt."""
    body: Dict[str, Any]
    status: ReportStatus
class ReportingApiEndpoint(TypedDict, total=True):
    url: str
    """The URL of the endpoint to which reports may be delivered."""
    groupName: str
    """Name of the endpoint group."""
class DeviceBoundSessionKey(TypedDict, total=True):
    """Unique identifier for a device bound session."""
    site: str
    """The site the session is set up for."""
    id: str
    """The id of the session."""
class DeviceBoundSessionWithUsage(TypedDict, total=True):
    """How a device bound session was used during a request."""
    sessionKey: DeviceBoundSessionKey
    """The key for the session."""
    usage: Literal["NotInScope", "InScopeRefreshNotYetNeeded", "InScopeRefreshNotAllowed", "ProactiveRefreshNotPossible", "ProactiveRefreshAttempted", "Deferred"]
    """How the session was used (or not used)."""
class DeviceBoundSessionCookieCraving(TypedDict, total=True):
    """A device bound session's cookie craving."""
    name: str
    """The name of the craving."""
    domain: str
    """The domain of the craving."""
    path: str
    """The path of the craving."""
    secure: bool
    """The Secure attribute of the craving attributes."""
    httpOnly: bool
    """The HttpOnly attribute of the craving attributes."""
    sameSite: NotRequired[CookieSameSite]
    """The SameSite attribute of the craving attributes."""
class DeviceBoundSessionUrlRule(TypedDict, total=True):
    """A device bound session's inclusion URL rule."""
    ruleType: Literal["Exclude", "Include"]
    """See comments on net::device_bound_sessions::SessionInclusionRules::UrlRule::rule_type."""
    hostPattern: str
    """See comments on net::device_bound_sessions::SessionInclusionRules::UrlRule::host_pattern."""
    pathPrefix: str
    """See comments on net::device_bound_sessions::SessionInclusionRules::UrlRule::path_prefix."""
class DeviceBoundSessionInclusionRules(TypedDict, total=True):
    """A device bound session's inclusion rules."""
    origin: str
    """See comments on net::device_bound_sessions::SessionInclusionRules::origin_."""
    includeSite: bool
    """Whether the whole site is included. See comments on net::device_bound_sessions::SessionInclusionRules::include_site_ for more details; this boolean is true if that value is populated."""
    urlRules: List[DeviceBoundSessionUrlRule]
    """See comments on net::device_bound_sessions::SessionInclusionRules::url_rules_."""
class DeviceBoundSession(TypedDict, total=True):
    """A device bound session."""
    key: DeviceBoundSessionKey
    """The site and session ID of the session."""
    refreshUrl: str
    """See comments on net::device_bound_sessions::Session::refresh_url_."""
    inclusionRules: DeviceBoundSessionInclusionRules
    """See comments on net::device_bound_sessions::Session::inclusion_rules_."""
    cookieCravings: List[DeviceBoundSessionCookieCraving]
    """See comments on net::device_bound_sessions::Session::cookie_cravings_."""
    expiryDate: TimeSinceEpoch
    """See comments on net::device_bound_sessions::Session::expiry_date_."""
    allowedRefreshInitiators: List[str]
    """See comments on net::device_bound_sessions::Session::allowed_refresh_initiators_."""
    cachedChallenge: NotRequired[str]
    """See comments on net::device_bound_sessions::Session::cached_challenge__."""
DeviceBoundSessionEventId = str
"""A unique identifier for a device bound session event."""
DeviceBoundSessionFetchResult = Literal['Success','KeyError','SigningError','ServerRequestedTermination','InvalidSessionId','InvalidChallenge','TooManyChallenges','InvalidFetcherUrl','InvalidRefreshUrl','TransientHttpError','ScopeOriginSameSiteMismatch','RefreshUrlSameSiteMismatch','MismatchedSessionId','MissingScope','NoCredentials','SubdomainRegistrationWellKnownUnavailable','SubdomainRegistrationUnauthorized','SubdomainRegistrationWellKnownMalformed','SessionProviderWellKnownUnavailable','RelyingPartyWellKnownUnavailable','FederatedKeyThumbprintMismatch','InvalidFederatedSessionUrl','InvalidFederatedKey','TooManyRelyingOriginLabels','BoundCookieSetForbidden','NetError','ProxyError','EmptySessionConfig','InvalidCredentialsConfig','InvalidCredentialsType','InvalidCredentialsEmptyName','InvalidCredentialsCookie','PersistentHttpError','RegistrationAttemptedChallenge','InvalidScopeOrigin','ScopeOriginContainsPath','RefreshInitiatorNotString','RefreshInitiatorInvalidHostPattern','InvalidScopeSpecification','MissingScopeSpecificationType','EmptyScopeSpecificationDomain','EmptyScopeSpecificationPath','InvalidScopeSpecificationType','InvalidScopeIncludeSite','MissingScopeIncludeSite','FederatedNotAuthorizedByProvider','FederatedNotAuthorizedByRelyingParty','SessionProviderWellKnownMalformed','SessionProviderWellKnownHasProviderOrigin','RelyingPartyWellKnownMalformed','RelyingPartyWellKnownHasRelyingOrigins','InvalidFederatedSessionProviderSessionMissing','InvalidFederatedSessionWrongProviderOrigin','InvalidCredentialsCookieCreationTime','InvalidCredentialsCookieName','InvalidCredentialsCookieParsing','InvalidCredentialsCookieUnpermittedAttribute','InvalidCredentialsCookieInvalidDomain','InvalidCredentialsCookiePrefix','InvalidScopeRulePath','InvalidScopeRuleHostPattern','ScopeRuleOriginScopedHostPatternMismatch','ScopeRuleSiteScopedHostPatternMismatch','SigningQuotaExceeded','InvalidConfigJson','InvalidFederatedSessionProviderFailedToRestoreKey','FailedToUnwrapKey','SessionDeletedDuringRefresh']
"""A fetch result for a device bound session creation or refresh."""
class DeviceBoundSessionFailedRequest(TypedDict, total=True):
    """Details about a failed device bound session network request."""
    requestUrl: str
    """The failed request URL."""
    netError: NotRequired[str]
    """The net error of the response if it was not OK."""
    responseError: NotRequired[int]
    """The response code if the net error was OK and the response code was not 200."""
    responseErrorBody: NotRequired[str]
    """The body of the response if the net error was OK, the response code was not 200, and the response body was not empty."""
class CreationEventDetails(TypedDict, total=True):
    """Session event details specific to creation."""
    fetchResult: DeviceBoundSessionFetchResult
    """The result of the fetch attempt."""
    newSession: NotRequired[DeviceBoundSession]
    """The session if there was a newly created session. This is populated for all successful creation events."""
    failedRequest: NotRequired[DeviceBoundSessionFailedRequest]
    """Details about a failed device bound session network request if there was one."""
class RefreshEventDetails(TypedDict, total=True):
    """Session event details specific to refresh."""
    refreshResult: Literal["Refreshed", "InitializedService", "Unreachable", "ServerError", "RefreshQuotaExceeded", "FatalError", "SigningQuotaExceeded"]
    """The result of a refresh."""
    wasFullyProactiveRefresh: bool
    """See comments on net::device_bound_sessions::RefreshEventResult::was_fully_proactive_refresh."""
    fetchResult: NotRequired[DeviceBoundSessionFetchResult]
    """If there was a fetch attempt, the result of that."""
    newSession: NotRequired[DeviceBoundSession]
    """The session display if there was a newly created session. This is populated for any refresh event that modifies the session config."""
    failedRequest: NotRequired[DeviceBoundSessionFailedRequest]
    """Details about a failed device bound session network request if there was one."""
class TerminationEventDetails(TypedDict, total=True):
    """Session event details specific to termination."""
    deletionReason: Literal["Expired", "FailedToRestoreKey", "FailedToUnwrapKey", "StoragePartitionCleared", "ClearBrowsingData", "ServerRequested", "InvalidSessionParams", "RefreshFatalError"]
    """The reason for a session being deleted."""
class ChallengeEventDetails(TypedDict, total=True):
    """Session event details specific to challenges."""
    challengeResult: Literal["Success", "NoSessionId", "NoSessionMatch", "CantSetBoundCookie"]
    """The result of a challenge."""
    challenge: str
    """The challenge set."""
class LoadNetworkResourcePageResult(TypedDict, total=True):
    """An object providing the result of a network resource load."""
    success: bool
    netError: NotRequired[float]
    """Optional values used for error reporting."""
    netErrorName: NotRequired[str]
    httpStatusCode: NotRequired[float]
    stream: NotRequired[StreamHandle]
    """If successful, one of the following two fields holds the result."""
    headers: NotRequired[Headers]
    """Response headers."""
class LoadNetworkResourceOptions(TypedDict, total=True):
    """An options object that may be extended later to better support CORS, CORB and streaming."""
    disableCache: bool
    includeCredentials: bool