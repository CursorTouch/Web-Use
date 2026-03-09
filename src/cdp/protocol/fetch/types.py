"""CDP Fetch Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.network.types import ResourceType

RequestId = str
"""Unique request identifier. Note that this does not identify individual HTTP requests that are part of a network request."""
RequestStage = Literal['Request','Response']
"""Stages of the request to handle. Request will intercept before the request is sent. Response will intercept after the response is received (but before response body is received)."""
class RequestPattern(TypedDict, total=False):
    urlPattern: NotRequired[str]
    """Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. Omitting is equivalent to "*"."""
    resourceType: NotRequired[ResourceType]
    """If set, only requests for matching resource types will be intercepted."""
    requestStage: NotRequired[RequestStage]
    """Stage at which to begin intercepting requests. Default is Request."""
class HeaderEntry(TypedDict, total=True):
    """Response HTTP header entry"""
    name: str
    value: str
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