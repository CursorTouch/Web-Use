"""CDP Page Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class PageMethods:
    """
    Methods for the Page domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Page methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def add_script_to_evaluate_on_new_document(self, params: addScriptToEvaluateOnNewDocumentParameters | None = None, session_id: str | None = None) -> addScriptToEvaluateOnNewDocumentReturns:
        """
    Evaluates given script in every frame upon creation (before loading frame's scripts).    
        Args:
            params (addScriptToEvaluateOnNewDocumentParameters, optional): Parameters for the addScriptToEvaluateOnNewDocument method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    addScriptToEvaluateOnNewDocumentReturns: The result of the addScriptToEvaluateOnNewDocument call.
        """
        return await self.client.send(method="Page.addScriptToEvaluateOnNewDocument", params=params, session_id=session_id)
    async def bring_to_front(self, params: bringToFrontParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Brings page to front (activates tab).    
        Args:
            params (bringToFrontParameters, optional): Parameters for the bringToFront method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the bringToFront call.
        """
        return await self.client.send(method="Page.bringToFront", params=params, session_id=session_id)
    async def capture_screenshot(self, params: captureScreenshotParameters | None = None, session_id: str | None = None) -> captureScreenshotReturns:
        """
    Capture page screenshot.    
        Args:
            params (captureScreenshotParameters, optional): Parameters for the captureScreenshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    captureScreenshotReturns: The result of the captureScreenshot call.
        """
        return await self.client.send(method="Page.captureScreenshot", params=params, session_id=session_id)
    async def capture_snapshot(self, params: captureSnapshotParameters | None = None, session_id: str | None = None) -> captureSnapshotReturns:
        """
    Returns a snapshot of the page as a string. For MHTML format, the serialization includes iframes, shadow DOM, external resources, and element-inline styles.    
        Args:
            params (captureSnapshotParameters, optional): Parameters for the captureSnapshot method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    captureSnapshotReturns: The result of the captureSnapshot call.
        """
        return await self.client.send(method="Page.captureSnapshot", params=params, session_id=session_id)
    async def create_isolated_world(self, params: createIsolatedWorldParameters | None = None, session_id: str | None = None) -> createIsolatedWorldReturns:
        """
    Creates an isolated world for the given frame.    
        Args:
            params (createIsolatedWorldParameters, optional): Parameters for the createIsolatedWorld method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    createIsolatedWorldReturns: The result of the createIsolatedWorld call.
        """
        return await self.client.send(method="Page.createIsolatedWorld", params=params, session_id=session_id)
    async def disable(self, params: disableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Disables page domain notifications.    
        Args:
            params (disableParameters, optional): Parameters for the disable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the disable call.
        """
        return await self.client.send(method="Page.disable", params=params, session_id=session_id)
    async def enable(self, params: enableParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables page domain notifications.    
        Args:
            params (enableParameters, optional): Parameters for the enable method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the enable call.
        """
        return await self.client.send(method="Page.enable", params=params, session_id=session_id)
    async def get_app_manifest(self, params: getAppManifestParameters | None = None, session_id: str | None = None) -> getAppManifestReturns:
        """
    Gets the processed manifest for this current document.   This API always waits for the manifest to be loaded.   If manifestId is provided, and it does not match the manifest of the     current document, this API errors out.   If there is not a loaded page, this API errors out immediately.    
        Args:
            params (getAppManifestParameters, optional): Parameters for the getAppManifest method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAppManifestReturns: The result of the getAppManifest call.
        """
        return await self.client.send(method="Page.getAppManifest", params=params, session_id=session_id)
    async def get_installability_errors(self, params: getInstallabilityErrorsParameters | None = None, session_id: str | None = None) -> getInstallabilityErrorsReturns:
        """
    No description available for getInstallabilityErrors.    
        Args:
            params (getInstallabilityErrorsParameters, optional): Parameters for the getInstallabilityErrors method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getInstallabilityErrorsReturns: The result of the getInstallabilityErrors call.
        """
        return await self.client.send(method="Page.getInstallabilityErrors", params=params, session_id=session_id)
    async def get_app_id(self, params: getAppIdParameters | None = None, session_id: str | None = None) -> getAppIdReturns:
        """
    Returns the unique (PWA) app id. Only returns values if the feature flag 'WebAppEnableManifestId' is enabled    
        Args:
            params (getAppIdParameters, optional): Parameters for the getAppId method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAppIdReturns: The result of the getAppId call.
        """
        return await self.client.send(method="Page.getAppId", params=params, session_id=session_id)
    async def get_ad_script_ancestry(self, params: getAdScriptAncestryParameters | None = None, session_id: str | None = None) -> getAdScriptAncestryReturns:
        """
    No description available for getAdScriptAncestry.    
        Args:
            params (getAdScriptAncestryParameters, optional): Parameters for the getAdScriptAncestry method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAdScriptAncestryReturns: The result of the getAdScriptAncestry call.
        """
        return await self.client.send(method="Page.getAdScriptAncestry", params=params, session_id=session_id)
    async def get_frame_tree(self, params: getFrameTreeParameters | None = None, session_id: str | None = None) -> getFrameTreeReturns:
        """
    Returns present frame tree structure.    
        Args:
            params (getFrameTreeParameters, optional): Parameters for the getFrameTree method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getFrameTreeReturns: The result of the getFrameTree call.
        """
        return await self.client.send(method="Page.getFrameTree", params=params, session_id=session_id)
    async def get_layout_metrics(self, params: getLayoutMetricsParameters | None = None, session_id: str | None = None) -> getLayoutMetricsReturns:
        """
    Returns metrics relating to the layouting of the page, such as viewport bounds/scale.    
        Args:
            params (getLayoutMetricsParameters, optional): Parameters for the getLayoutMetrics method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getLayoutMetricsReturns: The result of the getLayoutMetrics call.
        """
        return await self.client.send(method="Page.getLayoutMetrics", params=params, session_id=session_id)
    async def get_navigation_history(self, params: getNavigationHistoryParameters | None = None, session_id: str | None = None) -> getNavigationHistoryReturns:
        """
    Returns navigation history for the current page.    
        Args:
            params (getNavigationHistoryParameters, optional): Parameters for the getNavigationHistory method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getNavigationHistoryReturns: The result of the getNavigationHistory call.
        """
        return await self.client.send(method="Page.getNavigationHistory", params=params, session_id=session_id)
    async def reset_navigation_history(self, params: resetNavigationHistoryParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Resets navigation history for the current page.    
        Args:
            params (resetNavigationHistoryParameters, optional): Parameters for the resetNavigationHistory method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the resetNavigationHistory call.
        """
        return await self.client.send(method="Page.resetNavigationHistory", params=params, session_id=session_id)
    async def get_resource_content(self, params: getResourceContentParameters | None = None, session_id: str | None = None) -> getResourceContentReturns:
        """
    Returns content of the given resource.    
        Args:
            params (getResourceContentParameters, optional): Parameters for the getResourceContent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getResourceContentReturns: The result of the getResourceContent call.
        """
        return await self.client.send(method="Page.getResourceContent", params=params, session_id=session_id)
    async def get_resource_tree(self, params: getResourceTreeParameters | None = None, session_id: str | None = None) -> getResourceTreeReturns:
        """
    Returns present frame / resource tree structure.    
        Args:
            params (getResourceTreeParameters, optional): Parameters for the getResourceTree method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getResourceTreeReturns: The result of the getResourceTree call.
        """
        return await self.client.send(method="Page.getResourceTree", params=params, session_id=session_id)
    async def handle_java_script_dialog(self, params: handleJavaScriptDialogParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).    
        Args:
            params (handleJavaScriptDialogParameters, optional): Parameters for the handleJavaScriptDialog method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the handleJavaScriptDialog call.
        """
        return await self.client.send(method="Page.handleJavaScriptDialog", params=params, session_id=session_id)
    async def navigate(self, params: navigateParameters | None = None, session_id: str | None = None) -> navigateReturns:
        """
    Navigates current page to the given URL.    
        Args:
            params (navigateParameters, optional): Parameters for the navigate method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    navigateReturns: The result of the navigate call.
        """
        return await self.client.send(method="Page.navigate", params=params, session_id=session_id)
    async def navigate_to_history_entry(self, params: navigateToHistoryEntryParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Navigates current page to the given history entry.    
        Args:
            params (navigateToHistoryEntryParameters, optional): Parameters for the navigateToHistoryEntry method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the navigateToHistoryEntry call.
        """
        return await self.client.send(method="Page.navigateToHistoryEntry", params=params, session_id=session_id)
    async def print_to_pdf(self, params: printToPDFParameters | None = None, session_id: str | None = None) -> printToPDFReturns:
        """
    Print page as PDF.    
        Args:
            params (printToPDFParameters, optional): Parameters for the printToPDF method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    printToPDFReturns: The result of the printToPDF call.
        """
        return await self.client.send(method="Page.printToPDF", params=params, session_id=session_id)
    async def reload(self, params: reloadParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reloads given page optionally ignoring the cache.    
        Args:
            params (reloadParameters, optional): Parameters for the reload method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the reload call.
        """
        return await self.client.send(method="Page.reload", params=params, session_id=session_id)
    async def remove_script_to_evaluate_on_new_document(self, params: removeScriptToEvaluateOnNewDocumentParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Removes given script from the list.    
        Args:
            params (removeScriptToEvaluateOnNewDocumentParameters, optional): Parameters for the removeScriptToEvaluateOnNewDocument method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeScriptToEvaluateOnNewDocument call.
        """
        return await self.client.send(method="Page.removeScriptToEvaluateOnNewDocument", params=params, session_id=session_id)
    async def screencast_frame_ack(self, params: screencastFrameAckParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Acknowledges that a screencast frame has been received by the frontend.    
        Args:
            params (screencastFrameAckParameters, optional): Parameters for the screencastFrameAck method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the screencastFrameAck call.
        """
        return await self.client.send(method="Page.screencastFrameAck", params=params, session_id=session_id)
    async def search_in_resource(self, params: searchInResourceParameters | None = None, session_id: str | None = None) -> searchInResourceReturns:
        """
    Searches for given string in resource content.    
        Args:
            params (searchInResourceParameters, optional): Parameters for the searchInResource method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    searchInResourceReturns: The result of the searchInResource call.
        """
        return await self.client.send(method="Page.searchInResource", params=params, session_id=session_id)
    async def set_ad_blocking_enabled(self, params: setAdBlockingEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable Chrome's experimental ad filter on all sites.    
        Args:
            params (setAdBlockingEnabledParameters, optional): Parameters for the setAdBlockingEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAdBlockingEnabled call.
        """
        return await self.client.send(method="Page.setAdBlockingEnabled", params=params, session_id=session_id)
    async def set_bypass_csp(self, params: setBypassCSPParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable page Content Security Policy by-passing.    
        Args:
            params (setBypassCSPParameters, optional): Parameters for the setBypassCSP method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setBypassCSP call.
        """
        return await self.client.send(method="Page.setBypassCSP", params=params, session_id=session_id)
    async def get_permissions_policy_state(self, params: getPermissionsPolicyStateParameters | None = None, session_id: str | None = None) -> getPermissionsPolicyStateReturns:
        """
    Get Permissions Policy state on given frame.    
        Args:
            params (getPermissionsPolicyStateParameters, optional): Parameters for the getPermissionsPolicyState method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getPermissionsPolicyStateReturns: The result of the getPermissionsPolicyState call.
        """
        return await self.client.send(method="Page.getPermissionsPolicyState", params=params, session_id=session_id)
    async def get_origin_trials(self, params: getOriginTrialsParameters | None = None, session_id: str | None = None) -> getOriginTrialsReturns:
        """
    Get Origin Trials on given frame.    
        Args:
            params (getOriginTrialsParameters, optional): Parameters for the getOriginTrials method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getOriginTrialsReturns: The result of the getOriginTrials call.
        """
        return await self.client.send(method="Page.getOriginTrials", params=params, session_id=session_id)
    async def set_font_families(self, params: setFontFamiliesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set generic font families.    
        Args:
            params (setFontFamiliesParameters, optional): Parameters for the setFontFamilies method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setFontFamilies call.
        """
        return await self.client.send(method="Page.setFontFamilies", params=params, session_id=session_id)
    async def set_font_sizes(self, params: setFontSizesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set default font sizes.    
        Args:
            params (setFontSizesParameters, optional): Parameters for the setFontSizes method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setFontSizes call.
        """
        return await self.client.send(method="Page.setFontSizes", params=params, session_id=session_id)
    async def set_document_content(self, params: setDocumentContentParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets given markup as the document's HTML.    
        Args:
            params (setDocumentContentParameters, optional): Parameters for the setDocumentContent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDocumentContent call.
        """
        return await self.client.send(method="Page.setDocumentContent", params=params, session_id=session_id)
    async def set_lifecycle_events_enabled(self, params: setLifecycleEventsEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Controls whether page will emit lifecycle events.    
        Args:
            params (setLifecycleEventsEnabledParameters, optional): Parameters for the setLifecycleEventsEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setLifecycleEventsEnabled call.
        """
        return await self.client.send(method="Page.setLifecycleEventsEnabled", params=params, session_id=session_id)
    async def start_screencast(self, params: startScreencastParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Starts sending each frame using the `screencastFrame` event.    
        Args:
            params (startScreencastParameters, optional): Parameters for the startScreencast method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the startScreencast call.
        """
        return await self.client.send(method="Page.startScreencast", params=params, session_id=session_id)
    async def stop_loading(self, params: stopLoadingParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Force the page stop all navigations and pending resource fetches.    
        Args:
            params (stopLoadingParameters, optional): Parameters for the stopLoading method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopLoading call.
        """
        return await self.client.send(method="Page.stopLoading", params=params, session_id=session_id)
    async def crash(self, params: crashParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Crashes renderer on the IO thread, generates minidumps.    
        Args:
            params (crashParameters, optional): Parameters for the crash method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the crash call.
        """
        return await self.client.send(method="Page.crash", params=params, session_id=session_id)
    async def close(self, params: closeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Tries to close page, running its beforeunload hooks, if any.    
        Args:
            params (closeParameters, optional): Parameters for the close method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the close call.
        """
        return await self.client.send(method="Page.close", params=params, session_id=session_id)
    async def set_web_lifecycle_state(self, params: setWebLifecycleStateParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Tries to update the web lifecycle state of the page. It will transition the page to the given state according to: https://github.com/WICG/web-lifecycle/    
        Args:
            params (setWebLifecycleStateParameters, optional): Parameters for the setWebLifecycleState method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setWebLifecycleState call.
        """
        return await self.client.send(method="Page.setWebLifecycleState", params=params, session_id=session_id)
    async def stop_screencast(self, params: stopScreencastParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Stops sending each frame in the `screencastFrame`.    
        Args:
            params (stopScreencastParameters, optional): Parameters for the stopScreencast method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the stopScreencast call.
        """
        return await self.client.send(method="Page.stopScreencast", params=params, session_id=session_id)
    async def produce_compilation_cache(self, params: produceCompilationCacheParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests backend to produce compilation cache for the specified scripts. `scripts` are appended to the list of scripts for which the cache would be produced. The list may be reset during page navigation. When script with a matching URL is encountered, the cache is optionally produced upon backend discretion, based on internal heuristics. See also: `Page.compilationCacheProduced`.    
        Args:
            params (produceCompilationCacheParameters, optional): Parameters for the produceCompilationCache method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the produceCompilationCache call.
        """
        return await self.client.send(method="Page.produceCompilationCache", params=params, session_id=session_id)
    async def add_compilation_cache(self, params: addCompilationCacheParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Seeds compilation cache for given url. Compilation cache does not survive cross-process navigation.    
        Args:
            params (addCompilationCacheParameters, optional): Parameters for the addCompilationCache method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the addCompilationCache call.
        """
        return await self.client.send(method="Page.addCompilationCache", params=params, session_id=session_id)
    async def clear_compilation_cache(self, params: clearCompilationCacheParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears seeded compilation cache.    
        Args:
            params (clearCompilationCacheParameters, optional): Parameters for the clearCompilationCache method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearCompilationCache call.
        """
        return await self.client.send(method="Page.clearCompilationCache", params=params, session_id=session_id)
    async def set_spc_transaction_mode(self, params: setSPCTransactionModeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets the Secure Payment Confirmation transaction mode. https://w3c.github.io/secure-payment-confirmation/#sctn-automation-set-spc-transaction-mode    
        Args:
            params (setSPCTransactionModeParameters, optional): Parameters for the setSPCTransactionMode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSPCTransactionMode call.
        """
        return await self.client.send(method="Page.setSPCTransactionMode", params=params, session_id=session_id)
    async def set_rph_registration_mode(self, params: setRPHRegistrationModeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Extensions for Custom Handlers API: https://html.spec.whatwg.org/multipage/system-state.html#rph-automation    
        Args:
            params (setRPHRegistrationModeParameters, optional): Parameters for the setRPHRegistrationMode method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setRPHRegistrationMode call.
        """
        return await self.client.send(method="Page.setRPHRegistrationMode", params=params, session_id=session_id)
    async def generate_test_report(self, params: generateTestReportParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Generates a report for testing.    
        Args:
            params (generateTestReportParameters, optional): Parameters for the generateTestReport method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the generateTestReport call.
        """
        return await self.client.send(method="Page.generateTestReport", params=params, session_id=session_id)
    async def wait_for_debugger(self, params: waitForDebuggerParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.    
        Args:
            params (waitForDebuggerParameters, optional): Parameters for the waitForDebugger method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the waitForDebugger call.
        """
        return await self.client.send(method="Page.waitForDebugger", params=params, session_id=session_id)
    async def set_intercept_file_chooser_dialog(self, params: setInterceptFileChooserDialogParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Intercept file chooser requests and transfer control to protocol clients. When file chooser interception is enabled, native file chooser dialog is not shown. Instead, a protocol event `Page.fileChooserOpened` is emitted.    
        Args:
            params (setInterceptFileChooserDialogParameters, optional): Parameters for the setInterceptFileChooserDialog method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setInterceptFileChooserDialog call.
        """
        return await self.client.send(method="Page.setInterceptFileChooserDialog", params=params, session_id=session_id)
    async def set_prerendering_allowed(self, params: setPrerenderingAllowedParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enable/disable prerendering manually.  This command is a short-term solution for https://crbug.com/1440085. See https://docs.google.com/document/d/12HVmFxYj5Jc-eJr5OmWsa2bqTJsbgGLKI6ZIyx0_wpA for more details.  TODO(https://crbug.com/1440085): Remove this once Puppeteer supports tab targets.    
        Args:
            params (setPrerenderingAllowedParameters, optional): Parameters for the setPrerenderingAllowed method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPrerenderingAllowed call.
        """
        return await self.client.send(method="Page.setPrerenderingAllowed", params=params, session_id=session_id)
    async def get_annotated_page_content(self, params: getAnnotatedPageContentParameters | None = None, session_id: str | None = None) -> getAnnotatedPageContentReturns:
        """
    Get the annotated page content for the main frame. This is an experimental command that is subject to change.    
        Args:
            params (getAnnotatedPageContentParameters, optional): Parameters for the getAnnotatedPageContent method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getAnnotatedPageContentReturns: The result of the getAnnotatedPageContent call.
        """
        return await self.client.send(method="Page.getAnnotatedPageContent", params=params, session_id=session_id)