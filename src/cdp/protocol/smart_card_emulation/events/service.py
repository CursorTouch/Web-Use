"""CDP SmartCardEmulation Domain Events"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class SmartCardEmulationEvents:
    """
    Events for the SmartCardEmulation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the SmartCardEmulation events.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    def on_establish_context_requested(self, callback: Callable[[establishContextRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardEstablishContext| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: establishContextRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.establishContextRequested', callback)
    def on_release_context_requested(self, callback: Callable[[releaseContextRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardReleaseContext| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: releaseContextRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.releaseContextRequested', callback)
    def on_list_readers_requested(self, callback: Callable[[listReadersRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardListReaders| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: listReadersRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.listReadersRequested', callback)
    def on_get_status_change_requested(self, callback: Callable[[getStatusChangeRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardGetStatusChange| is called. Timeout is specified in milliseconds.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: getStatusChangeRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.getStatusChangeRequested', callback)
    def on_cancel_requested(self, callback: Callable[[cancelRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardCancel| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: cancelRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.cancelRequested', callback)
    def on_connect_requested(self, callback: Callable[[connectRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardConnect| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: connectRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.connectRequested', callback)
    def on_disconnect_requested(self, callback: Callable[[disconnectRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardDisconnect| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: disconnectRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.disconnectRequested', callback)
    def on_transmit_requested(self, callback: Callable[[transmitRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardTransmit| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: transmitRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.transmitRequested', callback)
    def on_control_requested(self, callback: Callable[[controlRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardControl| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: controlRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.controlRequested', callback)
    def on_get_attrib_requested(self, callback: Callable[[getAttribRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardGetAttrib| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: getAttribRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.getAttribRequested', callback)
    def on_set_attrib_requested(self, callback: Callable[[setAttribRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardSetAttrib| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: setAttribRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.setAttribRequested', callback)
    def on_status_requested(self, callback: Callable[[statusRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardStatus| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: statusRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.statusRequested', callback)
    def on_begin_transaction_requested(self, callback: Callable[[beginTransactionRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardBeginTransaction| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: beginTransactionRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.beginTransactionRequested', callback)
    def on_end_transaction_requested(self, callback: Callable[[endTransactionRequestedEvent, str | None], None] | None = None) -> None:
        """
    Fired when |SCardEndTransaction| is called.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction    
        Args:
            callback (callable, optional): Function called when the event is fired. 
                The callback receives (params: endTransactionRequestedEvent, session_id: str | None).
        """
        self.client.on('SmartCardEmulation.endTransactionRequested', callback)