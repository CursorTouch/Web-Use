"""CDP CSS Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import CSSMethods
from .events.service import CSSEvents

if TYPE_CHECKING:
    from ...service import Client

class CSS(CSSMethods, CSSEvents):
    """
    This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles) have an associated `id` used in subsequent operations on the related object. Each object type has a specific `id` structure, and those are not interchangeable between objects of different kinds. CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.
    """
    def __init__(self, client: Client):
        """
        Initialize the CSS domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        CSSMethods.__init__(self, client)
        CSSEvents.__init__(self, client)