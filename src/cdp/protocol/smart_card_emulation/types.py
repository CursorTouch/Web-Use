"""CDP SmartCardEmulation Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

ResultCode = Literal['success','removed-card','reset-card','unpowered-card','unresponsive-card','unsupported-card','reader-unavailable','sharing-violation','not-transacted','no-smartcard','proto-mismatch','system-cancelled','not-ready','cancelled','insufficient-buffer','invalid-handle','invalid-parameter','invalid-value','no-memory','timeout','unknown-reader','unsupported-feature','no-readers-available','service-stopped','no-service','comm-error','internal-error','server-too-busy','unexpected','shutdown','unknown-card','unknown']
"""Indicates the PC/SC error code.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__ErrorCodes.html Microsoft: https://learn.microsoft.com/en-us/windows/win32/secauthn/authentication-return-values"""
ShareMode = Literal['shared','exclusive','direct']
"""Maps to the |SCARD_SHARE_*| values."""
Disposition = Literal['leave-card','reset-card','unpower-card','eject-card']
"""Indicates what the reader should do with the card."""
ConnectionState = Literal['absent','present','swallowed','powered','negotiable','specific']
"""Maps to |SCARD_*| connection state values."""
class ReaderStateFlags(TypedDict, total=False):
    """Maps to the |SCARD_STATE_*| flags."""
    unaware: NotRequired[bool]
    ignore: NotRequired[bool]
    changed: NotRequired[bool]
    unknown: NotRequired[bool]
    unavailable: NotRequired[bool]
    empty: NotRequired[bool]
    present: NotRequired[bool]
    exclusive: NotRequired[bool]
    inuse: NotRequired[bool]
    mute: NotRequired[bool]
    unpowered: NotRequired[bool]
class ProtocolSet(TypedDict, total=False):
    """Maps to the |SCARD_PROTOCOL_*| flags."""
    t0: NotRequired[bool]
    t1: NotRequired[bool]
    raw: NotRequired[bool]
Protocol = Literal['t0','t1','raw']
"""Maps to the |SCARD_PROTOCOL_*| values."""
class ReaderStateIn(TypedDict, total=True):
    reader: str
    currentState: ReaderStateFlags
    currentInsertionCount: int
class ReaderStateOut(TypedDict, total=True):
    reader: str
    eventState: ReaderStateFlags
    eventCount: int
    atr: str