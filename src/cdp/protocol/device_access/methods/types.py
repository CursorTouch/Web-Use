"""CDP DeviceAccess Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.device_access.types import DeviceId
    from cdp.protocol.device_access.types import RequestId



class selectPromptParameters(TypedDict, total=True):
    id: RequestId
    deviceId: DeviceId
class cancelPromptParameters(TypedDict, total=True):
    id: RequestId