"""CDP Browser Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class BrowserMethods:
    """
    Methods for the Browser domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Browser methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def set_permission(self, params: setPermissionParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set permission settings for given embedding and embedded origins.    
        Args:
            params (setPermissionParameters, optional): Parameters for the setPermission method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPermission call.
        """
        return await self.client.send(method="Browser.setPermission", params=params, session_id=session_id)
    async def reset_permissions(self, params: resetPermissionsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Reset all permission management for all origins.    
        Args:
            params (resetPermissionsParameters, optional): Parameters for the resetPermissions method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the resetPermissions call.
        """
        return await self.client.send(method="Browser.resetPermissions", params=params, session_id=session_id)
    async def set_download_behavior(self, params: setDownloadBehaviorParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set the behavior when downloading a file.    
        Args:
            params (setDownloadBehaviorParameters, optional): Parameters for the setDownloadBehavior method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDownloadBehavior call.
        """
        return await self.client.send(method="Browser.setDownloadBehavior", params=params, session_id=session_id)
    async def cancel_download(self, params: cancelDownloadParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Cancel a download if in progress    
        Args:
            params (cancelDownloadParameters, optional): Parameters for the cancelDownload method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the cancelDownload call.
        """
        return await self.client.send(method="Browser.cancelDownload", params=params, session_id=session_id)
    async def close(self, params: closeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Close browser gracefully.    
        Args:
            params (closeParameters, optional): Parameters for the close method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the close call.
        """
        return await self.client.send(method="Browser.close", params=params, session_id=session_id)
    async def crash(self, params: crashParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Crashes browser on the main thread.    
        Args:
            params (crashParameters, optional): Parameters for the crash method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the crash call.
        """
        return await self.client.send(method="Browser.crash", params=params, session_id=session_id)
    async def crash_gpu_process(self, params: crashGpuProcessParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Crashes GPU process.    
        Args:
            params (crashGpuProcessParameters, optional): Parameters for the crashGpuProcess method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the crashGpuProcess call.
        """
        return await self.client.send(method="Browser.crashGpuProcess", params=params, session_id=session_id)
    async def get_version(self, params: getVersionParameters | None = None, session_id: str | None = None) -> getVersionReturns:
        """
    Returns version information.    
        Args:
            params (getVersionParameters, optional): Parameters for the getVersion method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getVersionReturns: The result of the getVersion call.
        """
        return await self.client.send(method="Browser.getVersion", params=params, session_id=session_id)
    async def get_browser_command_line(self, params: getBrowserCommandLineParameters | None = None, session_id: str | None = None) -> getBrowserCommandLineReturns:
        """
    Returns the command line switches for the browser process if, and only if --enable-automation is on the commandline.    
        Args:
            params (getBrowserCommandLineParameters, optional): Parameters for the getBrowserCommandLine method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getBrowserCommandLineReturns: The result of the getBrowserCommandLine call.
        """
        return await self.client.send(method="Browser.getBrowserCommandLine", params=params, session_id=session_id)
    async def get_histograms(self, params: getHistogramsParameters | None = None, session_id: str | None = None) -> getHistogramsReturns:
        """
    Get Chrome histograms.    
        Args:
            params (getHistogramsParameters, optional): Parameters for the getHistograms method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getHistogramsReturns: The result of the getHistograms call.
        """
        return await self.client.send(method="Browser.getHistograms", params=params, session_id=session_id)
    async def get_histogram(self, params: getHistogramParameters | None = None, session_id: str | None = None) -> getHistogramReturns:
        """
    Get a Chrome histogram by name.    
        Args:
            params (getHistogramParameters, optional): Parameters for the getHistogram method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getHistogramReturns: The result of the getHistogram call.
        """
        return await self.client.send(method="Browser.getHistogram", params=params, session_id=session_id)
    async def get_window_bounds(self, params: getWindowBoundsParameters | None = None, session_id: str | None = None) -> getWindowBoundsReturns:
        """
    Get position and size of the browser window.    
        Args:
            params (getWindowBoundsParameters, optional): Parameters for the getWindowBounds method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getWindowBoundsReturns: The result of the getWindowBounds call.
        """
        return await self.client.send(method="Browser.getWindowBounds", params=params, session_id=session_id)
    async def get_window_for_target(self, params: getWindowForTargetParameters | None = None, session_id: str | None = None) -> getWindowForTargetReturns:
        """
    Get the browser window that contains the devtools target.    
        Args:
            params (getWindowForTargetParameters, optional): Parameters for the getWindowForTarget method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getWindowForTargetReturns: The result of the getWindowForTarget call.
        """
        return await self.client.send(method="Browser.getWindowForTarget", params=params, session_id=session_id)
    async def set_window_bounds(self, params: setWindowBoundsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set position and/or size of the browser window.    
        Args:
            params (setWindowBoundsParameters, optional): Parameters for the setWindowBounds method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setWindowBounds call.
        """
        return await self.client.send(method="Browser.setWindowBounds", params=params, session_id=session_id)
    async def set_contents_size(self, params: setContentsSizeParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set size of the browser contents resizing browser window as necessary.    
        Args:
            params (setContentsSizeParameters, optional): Parameters for the setContentsSize method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setContentsSize call.
        """
        return await self.client.send(method="Browser.setContentsSize", params=params, session_id=session_id)
    async def set_dock_tile(self, params: setDockTileParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set dock tile details, platform-specific.    
        Args:
            params (setDockTileParameters, optional): Parameters for the setDockTile method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDockTile call.
        """
        return await self.client.send(method="Browser.setDockTile", params=params, session_id=session_id)
    async def execute_browser_command(self, params: executeBrowserCommandParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Invoke custom browser commands used by telemetry.    
        Args:
            params (executeBrowserCommandParameters, optional): Parameters for the executeBrowserCommand method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the executeBrowserCommand call.
        """
        return await self.client.send(method="Browser.executeBrowserCommand", params=params, session_id=session_id)
    async def add_privacy_sandbox_enrollment_override(self, params: addPrivacySandboxEnrollmentOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Allows a site to use privacy sandbox features that require enrollment without the site actually being enrolled. Only supported on page targets.    
        Args:
            params (addPrivacySandboxEnrollmentOverrideParameters, optional): Parameters for the addPrivacySandboxEnrollmentOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the addPrivacySandboxEnrollmentOverride call.
        """
        return await self.client.send(method="Browser.addPrivacySandboxEnrollmentOverride", params=params, session_id=session_id)
    async def add_privacy_sandbox_coordinator_key_config(self, params: addPrivacySandboxCoordinatorKeyConfigParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Configures encryption keys used with a given privacy sandbox API to talk to a trusted coordinator.  Since this is intended for test automation only, coordinatorOrigin must be a .test domain. No existing coordinator configuration for the origin may exist.    
        Args:
            params (addPrivacySandboxCoordinatorKeyConfigParameters, optional): Parameters for the addPrivacySandboxCoordinatorKeyConfig method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the addPrivacySandboxCoordinatorKeyConfig call.
        """
        return await self.client.send(method="Browser.addPrivacySandboxCoordinatorKeyConfig", params=params, session_id=session_id)