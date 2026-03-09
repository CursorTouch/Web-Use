"""CDP Log Methods Types"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.log.types import ViolationSetting




class startViolationsReportParameters(TypedDict, total=True):
    config: List[ViolationSetting]
    """Configuration for violations."""