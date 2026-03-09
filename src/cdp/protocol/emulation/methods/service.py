"""CDP Emulation Domain Methods"""
from __future__ import annotations
from ..types import *
from .types import *
from typing import Optional, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ....service import Client

class EmulationMethods:
    """
    Methods for the Emulation domain.
    """
    def __init__(self, client: Client):
        """
        Initialize the Emulation methods.
        
        Args:
            client (Client): The parent CDP client instance.
        """
        self.client = client

    async def clear_device_metrics_override(self, params: clearDeviceMetricsOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears the overridden device metrics.    
        Args:
            params (clearDeviceMetricsOverrideParameters, optional): Parameters for the clearDeviceMetricsOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearDeviceMetricsOverride call.
        """
        return await self.client.send(method="Emulation.clearDeviceMetricsOverride", params=params, session_id=session_id)
    async def clear_geolocation_override(self, params: clearGeolocationOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears the overridden Geolocation Position and Error.    
        Args:
            params (clearGeolocationOverrideParameters, optional): Parameters for the clearGeolocationOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearGeolocationOverride call.
        """
        return await self.client.send(method="Emulation.clearGeolocationOverride", params=params, session_id=session_id)
    async def reset_page_scale_factor(self, params: resetPageScaleFactorParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Requests that page scale factor is reset to initial values.    
        Args:
            params (resetPageScaleFactorParameters, optional): Parameters for the resetPageScaleFactor method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the resetPageScaleFactor call.
        """
        return await self.client.send(method="Emulation.resetPageScaleFactor", params=params, session_id=session_id)
    async def set_focus_emulation_enabled(self, params: setFocusEmulationEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables or disables simulating a focused and active page.    
        Args:
            params (setFocusEmulationEnabledParameters, optional): Parameters for the setFocusEmulationEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setFocusEmulationEnabled call.
        """
        return await self.client.send(method="Emulation.setFocusEmulationEnabled", params=params, session_id=session_id)
    async def set_auto_dark_mode_override(self, params: setAutoDarkModeOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Automatically render all web contents using a dark theme.    
        Args:
            params (setAutoDarkModeOverrideParameters, optional): Parameters for the setAutoDarkModeOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAutoDarkModeOverride call.
        """
        return await self.client.send(method="Emulation.setAutoDarkModeOverride", params=params, session_id=session_id)
    async def set_cpu_throttling_rate(self, params: setCPUThrottlingRateParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables CPU throttling to emulate slow CPUs.    
        Args:
            params (setCPUThrottlingRateParameters, optional): Parameters for the setCPUThrottlingRate method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setCPUThrottlingRate call.
        """
        return await self.client.send(method="Emulation.setCPUThrottlingRate", params=params, session_id=session_id)
    async def set_default_background_color_override(self, params: setDefaultBackgroundColorOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one.    
        Args:
            params (setDefaultBackgroundColorOverrideParameters, optional): Parameters for the setDefaultBackgroundColorOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDefaultBackgroundColorOverride call.
        """
        return await self.client.send(method="Emulation.setDefaultBackgroundColorOverride", params=params, session_id=session_id)
    async def set_safe_area_insets_override(self, params: setSafeAreaInsetsOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the respective variables to be undefined, even if previously overridden.    
        Args:
            params (setSafeAreaInsetsOverrideParameters, optional): Parameters for the setSafeAreaInsetsOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSafeAreaInsetsOverride call.
        """
        return await self.client.send(method="Emulation.setSafeAreaInsetsOverride", params=params, session_id=session_id)
    async def set_device_metrics_override(self, params: setDeviceMetricsOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).    
        Args:
            params (setDeviceMetricsOverrideParameters, optional): Parameters for the setDeviceMetricsOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDeviceMetricsOverride call.
        """
        return await self.client.send(method="Emulation.setDeviceMetricsOverride", params=params, session_id=session_id)
    async def set_device_posture_override(self, params: setDevicePostureOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Start reporting the given posture value to the Device Posture API. This override can also be set in setDeviceMetricsOverride().    
        Args:
            params (setDevicePostureOverrideParameters, optional): Parameters for the setDevicePostureOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDevicePostureOverride call.
        """
        return await self.client.send(method="Emulation.setDevicePostureOverride", params=params, session_id=session_id)
    async def clear_device_posture_override(self, params: clearDevicePostureOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears a device posture override set with either setDeviceMetricsOverride() or setDevicePostureOverride() and starts using posture information from the platform again. Does nothing if no override is set.    
        Args:
            params (clearDevicePostureOverrideParameters, optional): Parameters for the clearDevicePostureOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearDevicePostureOverride call.
        """
        return await self.client.send(method="Emulation.clearDevicePostureOverride", params=params, session_id=session_id)
    async def set_display_features_override(self, params: setDisplayFeaturesOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Start using the given display features to pupulate the Viewport Segments API. This override can also be set in setDeviceMetricsOverride().    
        Args:
            params (setDisplayFeaturesOverrideParameters, optional): Parameters for the setDisplayFeaturesOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDisplayFeaturesOverride call.
        """
        return await self.client.send(method="Emulation.setDisplayFeaturesOverride", params=params, session_id=session_id)
    async def clear_display_features_override(self, params: clearDisplayFeaturesOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears the display features override set with either setDeviceMetricsOverride() or setDisplayFeaturesOverride() and starts using display features from the platform again. Does nothing if no override is set.    
        Args:
            params (clearDisplayFeaturesOverrideParameters, optional): Parameters for the clearDisplayFeaturesOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearDisplayFeaturesOverride call.
        """
        return await self.client.send(method="Emulation.clearDisplayFeaturesOverride", params=params, session_id=session_id)
    async def set_scrollbars_hidden(self, params: setScrollbarsHiddenParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setScrollbarsHidden.    
        Args:
            params (setScrollbarsHiddenParameters, optional): Parameters for the setScrollbarsHidden method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setScrollbarsHidden call.
        """
        return await self.client.send(method="Emulation.setScrollbarsHidden", params=params, session_id=session_id)
    async def set_document_cookie_disabled(self, params: setDocumentCookieDisabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setDocumentCookieDisabled.    
        Args:
            params (setDocumentCookieDisabledParameters, optional): Parameters for the setDocumentCookieDisabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDocumentCookieDisabled call.
        """
        return await self.client.send(method="Emulation.setDocumentCookieDisabled", params=params, session_id=session_id)
    async def set_emit_touch_events_for_mouse(self, params: setEmitTouchEventsForMouseParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setEmitTouchEventsForMouse.    
        Args:
            params (setEmitTouchEventsForMouseParameters, optional): Parameters for the setEmitTouchEventsForMouse method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setEmitTouchEventsForMouse call.
        """
        return await self.client.send(method="Emulation.setEmitTouchEventsForMouse", params=params, session_id=session_id)
    async def set_emulated_media(self, params: setEmulatedMediaParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Emulates the given media type or media feature for CSS media queries.    
        Args:
            params (setEmulatedMediaParameters, optional): Parameters for the setEmulatedMedia method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setEmulatedMedia call.
        """
        return await self.client.send(method="Emulation.setEmulatedMedia", params=params, session_id=session_id)
    async def set_emulated_vision_deficiency(self, params: setEmulatedVisionDeficiencyParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Emulates the given vision deficiency.    
        Args:
            params (setEmulatedVisionDeficiencyParameters, optional): Parameters for the setEmulatedVisionDeficiency method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setEmulatedVisionDeficiency call.
        """
        return await self.client.send(method="Emulation.setEmulatedVisionDeficiency", params=params, session_id=session_id)
    async def set_emulated_os_text_scale(self, params: setEmulatedOSTextScaleParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Emulates the given OS text scale.    
        Args:
            params (setEmulatedOSTextScaleParameters, optional): Parameters for the setEmulatedOSTextScale method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setEmulatedOSTextScale call.
        """
        return await self.client.send(method="Emulation.setEmulatedOSTextScale", params=params, session_id=session_id)
    async def set_geolocation_override(self, params: setGeolocationOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides the Geolocation Position or Error. Omitting latitude, longitude or accuracy emulates position unavailable.    
        Args:
            params (setGeolocationOverrideParameters, optional): Parameters for the setGeolocationOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setGeolocationOverride call.
        """
        return await self.client.send(method="Emulation.setGeolocationOverride", params=params, session_id=session_id)
    async def get_overridden_sensor_information(self, params: getOverriddenSensorInformationParameters | None = None, session_id: str | None = None) -> getOverriddenSensorInformationReturns:
        """
    No description available for getOverriddenSensorInformation.    
        Args:
            params (getOverriddenSensorInformationParameters, optional): Parameters for the getOverriddenSensorInformation method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getOverriddenSensorInformationReturns: The result of the getOverriddenSensorInformation call.
        """
        return await self.client.send(method="Emulation.getOverriddenSensorInformation", params=params, session_id=session_id)
    async def set_sensor_override_enabled(self, params: setSensorOverrideEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides a platform sensor of a given type. If |enabled| is true, calls to Sensor.start() will use a virtual sensor as backend rather than fetching data from a real hardware sensor. Otherwise, existing virtual sensor-backend Sensor objects will fire an error event and new calls to Sensor.start() will attempt to use a real sensor instead.    
        Args:
            params (setSensorOverrideEnabledParameters, optional): Parameters for the setSensorOverrideEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSensorOverrideEnabled call.
        """
        return await self.client.send(method="Emulation.setSensorOverrideEnabled", params=params, session_id=session_id)
    async def set_sensor_override_readings(self, params: setSensorOverrideReadingsParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Updates the sensor readings reported by a sensor type previously overridden by setSensorOverrideEnabled.    
        Args:
            params (setSensorOverrideReadingsParameters, optional): Parameters for the setSensorOverrideReadings method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSensorOverrideReadings call.
        """
        return await self.client.send(method="Emulation.setSensorOverrideReadings", params=params, session_id=session_id)
    async def set_pressure_source_override_enabled(self, params: setPressureSourceOverrideEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides a pressure source of a given type, as used by the Compute Pressure API, so that updates to PressureObserver.observe() are provided via setPressureStateOverride instead of being retrieved from platform-provided telemetry data.    
        Args:
            params (setPressureSourceOverrideEnabledParameters, optional): Parameters for the setPressureSourceOverrideEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPressureSourceOverrideEnabled call.
        """
        return await self.client.send(method="Emulation.setPressureSourceOverrideEnabled", params=params, session_id=session_id)
    async def set_pressure_state_override(self, params: setPressureStateOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    TODO: OBSOLETE: To remove when setPressureDataOverride is merged. Provides a given pressure state that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled.    
        Args:
            params (setPressureStateOverrideParameters, optional): Parameters for the setPressureStateOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPressureStateOverride call.
        """
        return await self.client.send(method="Emulation.setPressureStateOverride", params=params, session_id=session_id)
    async def set_pressure_data_override(self, params: setPressureDataOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Provides a given pressure data set that will be processed and eventually be delivered to PressureObserver users. |source| must have been previously overridden by setPressureSourceOverrideEnabled.    
        Args:
            params (setPressureDataOverrideParameters, optional): Parameters for the setPressureDataOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPressureDataOverride call.
        """
        return await self.client.send(method="Emulation.setPressureDataOverride", params=params, session_id=session_id)
    async def set_idle_override(self, params: setIdleOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides the Idle state.    
        Args:
            params (setIdleOverrideParameters, optional): Parameters for the setIdleOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setIdleOverride call.
        """
        return await self.client.send(method="Emulation.setIdleOverride", params=params, session_id=session_id)
    async def clear_idle_override(self, params: clearIdleOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Clears Idle state overrides.    
        Args:
            params (clearIdleOverrideParameters, optional): Parameters for the clearIdleOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the clearIdleOverride call.
        """
        return await self.client.send(method="Emulation.clearIdleOverride", params=params, session_id=session_id)
    async def set_page_scale_factor(self, params: setPageScaleFactorParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Sets a specified page scale factor.    
        Args:
            params (setPageScaleFactorParameters, optional): Parameters for the setPageScaleFactor method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPageScaleFactor call.
        """
        return await self.client.send(method="Emulation.setPageScaleFactor", params=params, session_id=session_id)
    async def set_script_execution_disabled(self, params: setScriptExecutionDisabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Switches script execution in the page.    
        Args:
            params (setScriptExecutionDisabledParameters, optional): Parameters for the setScriptExecutionDisabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setScriptExecutionDisabled call.
        """
        return await self.client.send(method="Emulation.setScriptExecutionDisabled", params=params, session_id=session_id)
    async def set_touch_emulation_enabled(self, params: setTouchEmulationEnabledParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Enables touch on platforms which do not support them.    
        Args:
            params (setTouchEmulationEnabledParameters, optional): Parameters for the setTouchEmulationEnabled method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setTouchEmulationEnabled call.
        """
        return await self.client.send(method="Emulation.setTouchEmulationEnabled", params=params, session_id=session_id)
    async def set_virtual_time_policy(self, params: setVirtualTimePolicyParameters | None = None, session_id: str | None = None) -> setVirtualTimePolicyReturns:
        """
    Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget.    
        Args:
            params (setVirtualTimePolicyParameters, optional): Parameters for the setVirtualTimePolicy method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    setVirtualTimePolicyReturns: The result of the setVirtualTimePolicy call.
        """
        return await self.client.send(method="Emulation.setVirtualTimePolicy", params=params, session_id=session_id)
    async def set_locale_override(self, params: setLocaleOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides default host system locale with the specified one.    
        Args:
            params (setLocaleOverrideParameters, optional): Parameters for the setLocaleOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setLocaleOverride call.
        """
        return await self.client.send(method="Emulation.setLocaleOverride", params=params, session_id=session_id)
    async def set_timezone_override(self, params: setTimezoneOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Overrides default host system timezone with the specified one.    
        Args:
            params (setTimezoneOverrideParameters, optional): Parameters for the setTimezoneOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setTimezoneOverride call.
        """
        return await self.client.send(method="Emulation.setTimezoneOverride", params=params, session_id=session_id)
    async def set_disabled_image_types(self, params: setDisabledImageTypesParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setDisabledImageTypes.    
        Args:
            params (setDisabledImageTypesParameters, optional): Parameters for the setDisabledImageTypes method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDisabledImageTypes call.
        """
        return await self.client.send(method="Emulation.setDisabledImageTypes", params=params, session_id=session_id)
    async def set_data_saver_override(self, params: setDataSaverOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Override the value of navigator.connection.saveData    
        Args:
            params (setDataSaverOverrideParameters, optional): Parameters for the setDataSaverOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setDataSaverOverride call.
        """
        return await self.client.send(method="Emulation.setDataSaverOverride", params=params, session_id=session_id)
    async def set_hardware_concurrency_override(self, params: setHardwareConcurrencyOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    No description available for setHardwareConcurrencyOverride.    
        Args:
            params (setHardwareConcurrencyOverrideParameters, optional): Parameters for the setHardwareConcurrencyOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setHardwareConcurrencyOverride call.
        """
        return await self.client.send(method="Emulation.setHardwareConcurrencyOverride", params=params, session_id=session_id)
    async def set_user_agent_override(self, params: setUserAgentOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Allows overriding user agent with the given string. `userAgentMetadata` must be set for Client Hint headers to be sent.    
        Args:
            params (setUserAgentOverrideParameters, optional): Parameters for the setUserAgentOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setUserAgentOverride call.
        """
        return await self.client.send(method="Emulation.setUserAgentOverride", params=params, session_id=session_id)
    async def set_automation_override(self, params: setAutomationOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Allows overriding the automation flag.    
        Args:
            params (setAutomationOverrideParameters, optional): Parameters for the setAutomationOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setAutomationOverride call.
        """
        return await self.client.send(method="Emulation.setAutomationOverride", params=params, session_id=session_id)
    async def set_small_viewport_height_difference_override(self, params: setSmallViewportHeightDifferenceOverrideParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Allows overriding the difference between the small and large viewport sizes, which determine the value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames.    
        Args:
            params (setSmallViewportHeightDifferenceOverrideParameters, optional): Parameters for the setSmallViewportHeightDifferenceOverride method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setSmallViewportHeightDifferenceOverride call.
        """
        return await self.client.send(method="Emulation.setSmallViewportHeightDifferenceOverride", params=params, session_id=session_id)
    async def get_screen_infos(self, params: getScreenInfosParameters | None = None, session_id: str | None = None) -> getScreenInfosReturns:
        """
    Returns device's screen configuration. In headful mode, the physical screens configuration is returned, whereas in headless mode, a virtual headless screen configuration is provided instead.    
        Args:
            params (getScreenInfosParameters, optional): Parameters for the getScreenInfos method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    getScreenInfosReturns: The result of the getScreenInfos call.
        """
        return await self.client.send(method="Emulation.getScreenInfos", params=params, session_id=session_id)
    async def add_screen(self, params: addScreenParameters | None = None, session_id: str | None = None) -> addScreenReturns:
        """
    Add a new screen to the device. Only supported in headless mode.    
        Args:
            params (addScreenParameters, optional): Parameters for the addScreen method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    addScreenReturns: The result of the addScreen call.
        """
        return await self.client.send(method="Emulation.addScreen", params=params, session_id=session_id)
    async def update_screen(self, params: updateScreenParameters | None = None, session_id: str | None = None) -> updateScreenReturns:
        """
    Updates specified screen parameters. Only supported in headless mode.    
        Args:
            params (updateScreenParameters, optional): Parameters for the updateScreen method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    updateScreenReturns: The result of the updateScreen call.
        """
        return await self.client.send(method="Emulation.updateScreen", params=params, session_id=session_id)
    async def remove_screen(self, params: removeScreenParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Remove screen from the device. Only supported in headless mode.    
        Args:
            params (removeScreenParameters, optional): Parameters for the removeScreen method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the removeScreen call.
        """
        return await self.client.send(method="Emulation.removeScreen", params=params, session_id=session_id)
    async def set_primary_screen(self, params: setPrimaryScreenParameters | None = None, session_id: str | None = None) -> Dict[str, Any]:
        """
    Set primary screen. Only supported in headless mode. Note that this changes the coordinate system origin to the top-left of the new primary screen, updating the bounds and work areas of all existing screens accordingly.    
        Args:
            params (setPrimaryScreenParameters, optional): Parameters for the setPrimaryScreen method.
            session_id (str, optional): Target session ID for flat protocol usage.
            
        Returns:
    Dict[str, Any]: The result of the setPrimaryScreen call.
        """
        return await self.client.send(method="Emulation.setPrimaryScreen", params=params, session_id=session_id)