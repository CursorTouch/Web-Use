"""CDP SmartCardEmulation Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class SmartCardEmulationMethods:
    """
    Methods for the SmartCardEmulation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the SmartCardEmulation methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables the |SmartCardEmulation| domain.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="SmartCardEmulation.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables the |SmartCardEmulation| domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="SmartCardEmulation.disable", params=params, session_id=session_id)
    async def report_establish_context_result(self, params: reportEstablishContextResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a |SCardEstablishContext| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaa1b8970169fd4883a6dc4a8f43f19b67 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardestablishcontext    
        Args:
            params (reportEstablishContextResultParameters, optional): Parameters for the reportEstablishContextResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportEstablishContextResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportEstablishContextResult", params=params, session_id=session_id)
    async def report_release_context_result(self, params: reportReleaseContextResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a |SCardReleaseContext| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga6aabcba7744c5c9419fdd6404f73a934 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardreleasecontext    
        Args:
            params (reportReleaseContextResultParameters, optional): Parameters for the reportReleaseContextResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportReleaseContextResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportReleaseContextResult", params=params, session_id=session_id)
    async def report_list_readers_result(self, params: reportListReadersResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a |SCardListReaders| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga93b07815789b3cf2629d439ecf20f0d9 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardlistreadersa    
        Args:
            params (reportListReadersResultParameters, optional): Parameters for the reportListReadersResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportListReadersResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportListReadersResult", params=params, session_id=session_id)
    async def report_get_status_change_result(self, params: reportGetStatusChangeResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a |SCardGetStatusChange| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga33247d5d1257d59e55647c3bb717db24 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetstatuschangea    
        Args:
            params (reportGetStatusChangeResultParameters, optional): Parameters for the reportGetStatusChangeResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportGetStatusChangeResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportGetStatusChangeResult", params=params, session_id=session_id)
    async def report_begin_transaction_result(self, params: reportBeginTransactionResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the result of a |SCardBeginTransaction| call. On success, this creates a new transaction object.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaddb835dce01a0da1d6ca02d33ee7d861 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardbegintransaction    
        Args:
            params (reportBeginTransactionResultParameters, optional): Parameters for the reportBeginTransactionResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportBeginTransactionResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportBeginTransactionResult", params=params, session_id=session_id)
    async def report_plain_result(self, params: reportPlainResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a call that returns only a result code. Used for: |SCardCancel|, |SCardDisconnect|, |SCardSetAttrib|, |SCardEndTransaction|.  This maps to: 1. SCardCancel    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacbbc0c6d6c0cbbeb4f4debf6fbeeee6    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcancel  2. SCardDisconnect    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4be198045c73ec0deb79e66c0ca1738a    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scarddisconnect  3. SCardSetAttrib    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga060f0038a4ddfd5dd2b8fadf3c3a2e4f    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardsetattrib  4. SCardEndTransaction    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae8742473b404363e5c587f570d7e2f3b    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardendtransaction    
        Args:
            params (reportPlainResultParameters, optional): Parameters for the reportPlainResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportPlainResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportPlainResult", params=params, session_id=session_id)
    async def report_connect_result(self, params: reportConnectResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a |SCardConnect| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga4e515829752e0a8dbc4d630696a8d6a5 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardconnecta    
        Args:
            params (reportConnectResultParameters, optional): Parameters for the reportConnectResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportConnectResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportConnectResult", params=params, session_id=session_id)
    async def report_data_result(self, params: reportDataResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a call that sends back data on success. Used for |SCardTransmit|, |SCardControl|, and |SCardGetAttrib|.  This maps to: 1. SCardTransmit    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#ga9a2d77242a271310269065e64633ab99    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardtransmit  2. SCardControl    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gac3454d4657110fd7f753b2d3d8f4e32f    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardcontrol  3. SCardGetAttrib    PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gaacfec51917255b7a25b94c5104961602    Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardgetattrib    
        Args:
            params (reportDataResultParameters, optional): Parameters for the reportDataResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportDataResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportDataResult", params=params, session_id=session_id)
    async def report_status_result(self, params: reportStatusResultParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports the successful result of a |SCardStatus| call.  This maps to: PC/SC Lite: https://pcsclite.apdu.fr/api/group__API.html#gae49c3c894ad7ac12a5b896bde70d0382 Microsoft: https://learn.microsoft.com/en-us/windows/win32/api/winscard/nf-winscard-scardstatusa    
        Args:
            params (reportStatusResultParameters, optional): Parameters for the reportStatusResult method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportStatusResult call.
        """
        return await self.client.send(method="SmartCardEmulation.reportStatusResult", params=params, session_id=session_id)
    async def report_error(self, params: reportErrorParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reports an error result for the given request.    
        Args:
            params (reportErrorParameters, optional): Parameters for the reportError method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reportError call.
        """
        return await self.client.send(method="SmartCardEmulation.reportError", params=params, session_id=session_id)