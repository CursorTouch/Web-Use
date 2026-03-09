"""CDP FileSystem Domain"""
from __future__ import annotations
from typing import TYPE_CHECKING
from .methods.service import FileSystemMethods
from .events.service import FileSystemEvents

if TYPE_CHECKING:
    from ...service import Client

class FileSystem(FileSystemMethods, FileSystemEvents):
    """
    Access the FileSystem domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the FileSystem domain.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        FileSystemMethods.__init__(self, client)
        FileSystemEvents.__init__(self, client)