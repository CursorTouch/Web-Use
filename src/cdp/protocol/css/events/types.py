"""CDP CSS Events"""
from __future__ import annotations
from typing import TypedDict, NotRequired, Required, Literal, Any, Dict, Union, Optional, List, Set, Tuple

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cdp.protocol.css.types import CSSStyleSheetHeader
    from cdp.protocol.css.types import FontFace
    from cdp.protocol.dom.types import NodeId
    from cdp.protocol.dom.types import StyleSheetId

class fontsUpdatedEvent(TypedDict, total=False):
    font: NotRequired[FontFace]
    """The web font that has loaded."""
class mediaQueryResultChangedEvent(TypedDict, total=True):
    pass
class styleSheetAddedEvent(TypedDict, total=True):
    header: CSSStyleSheetHeader
    """Added stylesheet metainfo."""
class styleSheetChangedEvent(TypedDict, total=True):
    styleSheetId: StyleSheetId
class styleSheetRemovedEvent(TypedDict, total=True):
    styleSheetId: StyleSheetId
    """Identifier of the removed stylesheet."""
class computedStyleUpdatedEvent(TypedDict, total=True):
    nodeId: NodeId
    """The node id that has updated computed styles."""