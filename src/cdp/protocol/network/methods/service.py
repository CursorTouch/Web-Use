"""CDP Network Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class NetworkMethods:
    """
    Methods for the Network domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Network methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def set_accepted_encodings(self, params: setAcceptedEncodingsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.    
        Args:
            params (setAcceptedEncodingsParameters, optional): Parameters for the setAcceptedEncodings method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAcceptedEncodings call.
        """
        return await self.client.send(method="Network.setAcceptedEncodings", params=params, session_id=session_id)
    async def clear_accepted_encodings_override(self, params: clearAcceptedEncodingsOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears accepted encodings set by setAcceptedEncodings    
        Args:
            params (clearAcceptedEncodingsOverrideParameters, optional): Parameters for the clearAcceptedEncodingsOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearAcceptedEncodingsOverride call.
        """
        return await self.client.send(method="Network.clearAcceptedEncodingsOverride", params=params, session_id=session_id)
    async def clear_browser_cache(self, params: clearBrowserCacheParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears browser cache.    
        Args:
            params (clearBrowserCacheParameters, optional): Parameters for the clearBrowserCache method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearBrowserCache call.
        """
        return await self.client.send(method="Network.clearBrowserCache", params=params, session_id=session_id)
    async def clear_browser_cookies(self, params: clearBrowserCookiesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears browser cookies.    
        Args:
            params (clearBrowserCookiesParameters, optional): Parameters for the clearBrowserCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearBrowserCookies call.
        """
        return await self.client.send(method="Network.clearBrowserCookies", params=params, session_id=session_id)
    async def delete_cookies(self, params: deleteCookiesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Deletes browser cookies with matching name and url or domain/path/partitionKey pair.    
        Args:
            params (deleteCookiesParameters, optional): Parameters for the deleteCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the deleteCookies call.
        """
        return await self.client.send(method="Network.deleteCookies", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables network tracking, prevents network events from being sent to the client.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Network.disable", params=params, session_id=session_id)
    async def emulate_network_conditions_by_rule(self, params: emulateNetworkConditionsByRuleParameters | None = None, session_id: str | None = None) -> emulateNetworkConditionsByRuleReturns:
        """
    Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to explicitly modify `navigator` behavior.    
        Args:
            params (emulateNetworkConditionsByRuleParameters, optional): Parameters for the emulateNetworkConditionsByRule method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    emulateNetworkConditionsByRuleReturns: The result of the emulateNetworkConditionsByRule call.
        """
        return await self.client.send(method="Network.emulateNetworkConditionsByRule", params=params, session_id=session_id)
    async def override_network_state(self, params: overrideNetworkStateParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Override the state of navigator.onLine and navigator.connection.    
        Args:
            params (overrideNetworkStateParameters, optional): Parameters for the overrideNetworkState method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the overrideNetworkState call.
        """
        return await self.client.send(method="Network.overrideNetworkState", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables network tracking, network events will now be delivered to the client.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Network.enable", params=params, session_id=session_id)
    async def configure_durable_messages(self, params: configureDurableMessagesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Configures storing response bodies outside of renderer, so that these survive a cross-process navigation. If maxTotalBufferSize is not set, durable messages are disabled.    
        Args:
            params (configureDurableMessagesParameters, optional): Parameters for the configureDurableMessages method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the configureDurableMessages call.
        """
        return await self.client.send(method="Network.configureDurableMessages", params=params, session_id=session_id)
    async def get_certificate(self, params: getCertificateParameters | None = None, session_id: str | None = None) -> getCertificateReturns:
        """
    Returns the DER-encoded certificate.    
        Args:
            params (getCertificateParameters, optional): Parameters for the getCertificate method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCertificateReturns: The result of the getCertificate call.
        """
        return await self.client.send(method="Network.getCertificate", params=params, session_id=session_id)
    async def get_cookies(self, params: getCookiesParameters | None = None, session_id: str | None = None) -> getCookiesReturns:
        """
    Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the `cookies` field.    
        Args:
            params (getCookiesParameters, optional): Parameters for the getCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getCookiesReturns: The result of the getCookies call.
        """
        return await self.client.send(method="Network.getCookies", params=params, session_id=session_id)
    async def get_response_body(self, params: getResponseBodyParameters | None = None, session_id: str | None = None) -> getResponseBodyReturns:
        """
    Returns content served for the given request.    
        Args:
            params (getResponseBodyParameters, optional): Parameters for the getResponseBody method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getResponseBodyReturns: The result of the getResponseBody call.
        """
        return await self.client.send(method="Network.getResponseBody", params=params, session_id=session_id)
    async def get_request_post_data(self, params: getRequestPostDataParameters | None = None, session_id: str | None = None) -> getRequestPostDataReturns:
        """
    Returns post data sent with the request. Returns an error when no data was sent with the request.    
        Args:
            params (getRequestPostDataParameters, optional): Parameters for the getRequestPostData method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getRequestPostDataReturns: The result of the getRequestPostData call.
        """
        return await self.client.send(method="Network.getRequestPostData", params=params, session_id=session_id)
    async def get_response_body_for_interception(self, params: getResponseBodyForInterceptionParameters | None = None, session_id: str | None = None) -> getResponseBodyForInterceptionReturns:
        """
    Returns content served for the given currently intercepted request.    
        Args:
            params (getResponseBodyForInterceptionParameters, optional): Parameters for the getResponseBodyForInterception method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getResponseBodyForInterceptionReturns: The result of the getResponseBodyForInterception call.
        """
        return await self.client.send(method="Network.getResponseBodyForInterception", params=params, session_id=session_id)
    async def take_response_body_for_interception_as_stream(self, params: takeResponseBodyForInterceptionAsStreamParameters | None = None, session_id: str | None = None) -> takeResponseBodyForInterceptionAsStreamReturns:
        """
    Returns a handle to the stream representing the response body. Note that after this command, the intercepted request can't be continued as is -- you either need to cancel it or to provide the response body. The stream only supports sequential read, IO.read will fail if the position is specified.    
        Args:
            params (takeResponseBodyForInterceptionAsStreamParameters, optional): Parameters for the takeResponseBodyForInterceptionAsStream method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    takeResponseBodyForInterceptionAsStreamReturns: The result of the takeResponseBodyForInterceptionAsStream call.
        """
        return await self.client.send(method="Network.takeResponseBodyForInterceptionAsStream", params=params, session_id=session_id)
    async def replay_xhr(self, params: replayXHRParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password.    
        Args:
            params (replayXHRParameters, optional): Parameters for the replayXHR method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the replayXHR call.
        """
        return await self.client.send(method="Network.replayXHR", params=params, session_id=session_id)
    async def search_in_response_body(self, params: searchInResponseBodyParameters | None = None, session_id: str | None = None) -> searchInResponseBodyReturns:
        """
    Searches for given string in response content.    
        Args:
            params (searchInResponseBodyParameters, optional): Parameters for the searchInResponseBody method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    searchInResponseBodyReturns: The result of the searchInResponseBody call.
        """
        return await self.client.send(method="Network.searchInResponseBody", params=params, session_id=session_id)
    async def set_blocked_ur_ls(self, params: setBlockedURLsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Blocks URLs from loading.    
        Args:
            params (setBlockedURLsParameters, optional): Parameters for the setBlockedURLs method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBlockedURLs call.
        """
        return await self.client.send(method="Network.setBlockedURLs", params=params, session_id=session_id)
    async def set_bypass_service_worker(self, params: setBypassServiceWorkerParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Toggles ignoring of service worker for each request.    
        Args:
            params (setBypassServiceWorkerParameters, optional): Parameters for the setBypassServiceWorker method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBypassServiceWorker call.
        """
        return await self.client.send(method="Network.setBypassServiceWorker", params=params, session_id=session_id)
    async def set_cache_disabled(self, params: setCacheDisabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Toggles ignoring cache for each request. If `true`, cache will not be used.    
        Args:
            params (setCacheDisabledParameters, optional): Parameters for the setCacheDisabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCacheDisabled call.
        """
        return await self.client.send(method="Network.setCacheDisabled", params=params, session_id=session_id)
    async def set_cookie(self, params: setCookieParameters | None = None, session_id: str | None = None) -> setCookieReturns:
        """
    Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.    
        Args:
            params (setCookieParameters, optional): Parameters for the setCookie method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setCookieReturns: The result of the setCookie call.
        """
        return await self.client.send(method="Network.setCookie", params=params, session_id=session_id)
    async def set_cookies(self, params: setCookiesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets given cookies.    
        Args:
            params (setCookiesParameters, optional): Parameters for the setCookies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCookies call.
        """
        return await self.client.send(method="Network.setCookies", params=params, session_id=session_id)
    async def set_extra_http_headers(self, params: setExtraHTTPHeadersParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Specifies whether to always send extra HTTP headers with the requests from this page.    
        Args:
            params (setExtraHTTPHeadersParameters, optional): Parameters for the setExtraHTTPHeaders method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setExtraHTTPHeaders call.
        """
        return await self.client.send(method="Network.setExtraHTTPHeaders", params=params, session_id=session_id)
    async def set_attach_debug_stack(self, params: setAttachDebugStackParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Specifies whether to attach a page script stack id in requests    
        Args:
            params (setAttachDebugStackParameters, optional): Parameters for the setAttachDebugStack method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAttachDebugStack call.
        """
        return await self.client.send(method="Network.setAttachDebugStack", params=params, session_id=session_id)
    async def set_user_agent_override(self, params: setUserAgentOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Allows overriding user agent with the given string.    
        Args:
            params (setUserAgentOverrideParameters, optional): Parameters for the setUserAgentOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setUserAgentOverride call.
        """
        return await self.client.send(method="Network.setUserAgentOverride", params=params, session_id=session_id)
    async def stream_resource_content(self, params: streamResourceContentParameters | None = None, session_id: str | None = None) -> streamResourceContentReturns:
        """
    Enables streaming of the response for the given requestId. If enabled, the dataReceived event contains the data that was received during streaming.    
        Args:
            params (streamResourceContentParameters, optional): Parameters for the streamResourceContent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    streamResourceContentReturns: The result of the streamResourceContent call.
        """
        return await self.client.send(method="Network.streamResourceContent", params=params, session_id=session_id)
    async def get_security_isolation_status(self, params: getSecurityIsolationStatusParameters | None = None, session_id: str | None = None) -> getSecurityIsolationStatusReturns:
        """
    Returns information about the COEP/COOP isolation status.    
        Args:
            params (getSecurityIsolationStatusParameters, optional): Parameters for the getSecurityIsolationStatus method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getSecurityIsolationStatusReturns: The result of the getSecurityIsolationStatus call.
        """
        return await self.client.send(method="Network.getSecurityIsolationStatus", params=params, session_id=session_id)
    async def enable_reporting_api(self, params: enableReportingApiParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client. Enabling triggers 'reportingApiReportAdded' for all existing reports.    
        Args:
            params (enableReportingApiParameters, optional): Parameters for the enableReportingApi method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enableReportingApi call.
        """
        return await self.client.send(method="Network.enableReportingApi", params=params, session_id=session_id)
    async def enable_device_bound_sessions(self, params: enableDeviceBoundSessionsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets up tracking device bound sessions and fetching of initial set of sessions.    
        Args:
            params (enableDeviceBoundSessionsParameters, optional): Parameters for the enableDeviceBoundSessions method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enableDeviceBoundSessions call.
        """
        return await self.client.send(method="Network.enableDeviceBoundSessions", params=params, session_id=session_id)
    async def fetch_schemeful_site(self, params: fetchSchemefulSiteParameters | None = None, session_id: str | None = None) -> fetchSchemefulSiteReturns:
        """
    Fetches the schemeful site for a specific origin.    
        Args:
            params (fetchSchemefulSiteParameters, optional): Parameters for the fetchSchemefulSite method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    fetchSchemefulSiteReturns: The result of the fetchSchemefulSite call.
        """
        return await self.client.send(method="Network.fetchSchemefulSite", params=params, session_id=session_id)
    async def load_network_resource(self, params: loadNetworkResourceParameters | None = None, session_id: str | None = None) -> loadNetworkResourceReturns:
        """
    Fetches the resource and returns the content.    
        Args:
            params (loadNetworkResourceParameters, optional): Parameters for the loadNetworkResource method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    loadNetworkResourceReturns: The result of the loadNetworkResource call.
        """
        return await self.client.send(method="Network.loadNetworkResource", params=params, session_id=session_id)
    async def set_cookie_controls(self, params: setCookieControlsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets Controls for third-party cookie access Page reload is required before the new cookie behavior will be observed    
        Args:
            params (setCookieControlsParameters, optional): Parameters for the setCookieControls method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCookieControls call.
        """
        return await self.client.send(method="Network.setCookieControls", params=params, session_id=session_id)