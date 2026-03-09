"""CDP WebAuthn Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class WebAuthnMethods:
    """
    Methods for the WebAuthn domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the WebAuthn methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable the WebAuthn domain and start intercepting credential storage and retrieval with a virtual authenticator.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="WebAuthn.enable", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disable the WebAuthn domain.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="WebAuthn.disable", params=params, session_id=session_id)
    async def add_virtual_authenticator(self, params: addVirtualAuthenticatorParameters | None = None, session_id: str | None = None) -> addVirtualAuthenticatorReturns:
        """
    Creates and adds a virtual authenticator.    
        Args:
            params (addVirtualAuthenticatorParameters, optional): Parameters for the addVirtualAuthenticator method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    addVirtualAuthenticatorReturns: The result of the addVirtualAuthenticator call.
        """
        return await self.client.send(method="WebAuthn.addVirtualAuthenticator", params=params, session_id=session_id)
    async def set_response_override_bits(self, params: setResponseOverrideBitsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Resets parameters isBogusSignature, isBadUV, isBadUP to false if they are not present.    
        Args:
            params (setResponseOverrideBitsParameters, optional): Parameters for the setResponseOverrideBits method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setResponseOverrideBits call.
        """
        return await self.client.send(method="WebAuthn.setResponseOverrideBits", params=params, session_id=session_id)
    async def remove_virtual_authenticator(self, params: removeVirtualAuthenticatorParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes the given authenticator.    
        Args:
            params (removeVirtualAuthenticatorParameters, optional): Parameters for the removeVirtualAuthenticator method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeVirtualAuthenticator call.
        """
        return await self.client.send(method="WebAuthn.removeVirtualAuthenticator", params=params, session_id=session_id)
    async def add_credential(self, params: addCredentialParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Adds the credential to the specified authenticator.    
        Args:
            params (addCredentialParameters, optional): Parameters for the addCredential method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the addCredential call.
        """
        return await self.client.send(method="WebAuthn.addCredential", params=params, session_id=session_id)
    async def get_credential(self, params: getCredentialParameters | None = None, session_id: str | None = None) -> getCredentialReturns:
        """
    Returns a single credential stored in the given virtual authenticator that matches the credential ID.    
        Args:
            params (getCredentialParameters, optional): Parameters for the getCredential method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCredentialReturns: The result of the getCredential call.
        """
        return await self.client.send(method="WebAuthn.getCredential", params=params, session_id=session_id)
    async def get_credentials(self, params: getCredentialsParameters | None = None, session_id: str | None = None) -> getCredentialsReturns:
        """
    Returns all the credentials stored in the given virtual authenticator.    
        Args:
            params (getCredentialsParameters, optional): Parameters for the getCredentials method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCredentialsReturns: The result of the getCredentials call.
        """
        return await self.client.send(method="WebAuthn.getCredentials", params=params, session_id=session_id)
    async def remove_credential(self, params: removeCredentialParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes a credential from the authenticator.    
        Args:
            params (removeCredentialParameters, optional): Parameters for the removeCredential method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeCredential call.
        """
        return await self.client.send(method="WebAuthn.removeCredential", params=params, session_id=session_id)
    async def clear_credentials(self, params: clearCredentialsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears all the credentials from the specified device.    
        Args:
            params (clearCredentialsParameters, optional): Parameters for the clearCredentials method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearCredentials call.
        """
        return await self.client.send(method="WebAuthn.clearCredentials", params=params, session_id=session_id)
    async def set_user_verified(self, params: setUserVerifiedParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets whether User Verification succeeds or fails for an authenticator. The default is true.    
        Args:
            params (setUserVerifiedParameters, optional): Parameters for the setUserVerified method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setUserVerified call.
        """
        return await self.client.send(method="WebAuthn.setUserVerified", params=params, session_id=session_id)
    async def set_automatic_presence_simulation(self, params: setAutomaticPresenceSimulationParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator. The default is true.    
        Args:
            params (setAutomaticPresenceSimulationParameters, optional): Parameters for the setAutomaticPresenceSimulation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAutomaticPresenceSimulation call.
        """
        return await self.client.send(method="WebAuthn.setAutomaticPresenceSimulation", params=params, session_id=session_id)
    async def set_credential_properties(self, params: setCredentialPropertiesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Allows setting credential properties. https://w3c.github.io/webauthn/#sctn-automation-set-credential-properties    
        Args:
            params (setCredentialPropertiesParameters, optional): Parameters for the setCredentialProperties method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCredentialProperties call.
        """
        return await self.client.send(method="WebAuthn.setCredentialProperties", params=params, session_id=session_id)