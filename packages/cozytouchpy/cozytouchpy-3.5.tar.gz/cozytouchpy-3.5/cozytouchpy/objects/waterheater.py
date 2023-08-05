"""Describe objects for cozytouch."""
import logging

from cozytouchpy.constant import DeviceCommand as dc, DeviceState as ds, DeviceType as dt, ModeState, OnOffState
from ..exception import CozytouchException
from .device import CozytouchDevice

logger = logging.getLogger(__name__)


class CozytouchWaterHeater(CozytouchDevice):
    """Water Heater."""

    @property
    def is_on(self):
        """Is alive."""
        return self.operating_mode != ModeState.STANDBY

    @property
    def operating_mode(self):
        """Return operation mode."""
        if self.widget == dt.APC_WATER_HEATER:
            return self.get_state(ds.PASS_APC_DHW_MODE_STATE)
        return self.get_state(ds.DHW_MODE_STATE)

    @property
    def operating_mode_list(self):
        """Return operating mode list."""
        if self.widget == dt.APC_WATER_HEATER:
            return self.get_definition(ds.PASS_APC_DHW_MODE_STATE)
        return self.get_definition(ds.DHW_MODE_STATE)

    @property
    def current_temperature(self):
        """Return temperature (middle water heater)."""
        return self.get_state(ds.MIDDLE_WATER_TEMPERATURE_STATE)

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        if self.widget == dt.APC_WATER_HEATER:
            return self.get_state(ds.TARGET_DHW_TEMPERATURE_STATE)
        return self.get_state(ds.TARGET_TEMPERATURE_STATE)

    @property
    def is_away_mode(self):
        """Return true if away mode is on."""
        if self.widget == dt.WATER_HEATER:
            return self.get_state(ds.OPERATING_MODE_STATE).get('absence') == OnOffState.ON
        if self.widget == dt.PASS_APC_DHW:
            return self.get_state(ds.PASS_APC_DHW_PROFILE_STATE) == "absence"
        return self.get_state(ds.DHW_ABSENCE_MODE_STATE) == OnOffState.ON

    @property
    def is_boost_mode(self):
        """Return boot enable."""
        if self.widget == dt.WATER_HEATER:
            return self.get_state(ds.OPERATING_MODE_STATE).get('relaunch') == OnOffState.ON
        if self.widget == dt.APC_WATER_HEATER:
            return self.get_state(ds.BOOST_ON_OFF_STATE) == OnOffState.ON
        return self.get_state(ds.OPERATING_MODE_STATE) == OnOffState.ON

    @property
    def supported_states(self) -> dict:
        """Supported states."""
        supported_states = [state["name"] for state in self.states]
        for sensor in self.sensors:
            sensor_states = [state["name"] for state in sensor.states]
            supported_states = list(set(supported_states + sensor_states))
        return supported_states

    def is_state_supported(self, state):
        """Return is supported ."""
        return state in self.supported_states

    async def set_operating_mode(self, mode):
        """Set operating mode."""
        if self.widget == dt.APC_WATER_HEATER:
            await self.set_mode(dc.SET_PASS_APC_DHW_MODE, mode)
        await self.set_mode(dc.SET_DWH_MODE, mode)

    async def set_away_mode(self, duration):
        """Set away mode."""
        if self.controllable_name == dt.DHW_V2_FLATC2_IO:
            if int(duration) == 0:
                await self.set_mode(dc.SET_ABSENCE_MODE, OnOffState.OFF)
            else:
                await self.set_mode(dc.SET_ABSENCE_MODE, OnOffState.ON)
        else:
            if int(duration) == 0:
                await self.set_mode(dc.SET_CURRENT_OPERATING_MODE, {"relaunch": "off", "absence": "off"})
            else:
                await self.set_mode(dc.SET_AWAYS_MODE_DURATION, duration)
                await self.set_mode(dc.SET_CURRENT_OPERATING_MODE, {"relaunch": "off", "absence": "on"})

    async def set_boost_mode(self, duration):
        """Set Boost mode."""
        if self.widget == dt.APC_WATER_HEATER:
            if int(duration) == 0:
                await self.set_mode(dc.SET_BOOST_MODE_DURATION, OnOffState.OFF)
            else:
                await self.set_mode(dc.SET_BOOST_MODE_DURATION, OnOffState.ON)
        else:
            if int(duration) == 0:
                await self.set_mode(dc.SET_CURRENT_OPERATING_MODE, {"relaunch": "off", "absence": "off"})
            else:
                await self.set_mode(dc.SET_BOOST_MODE_DURATION, duration)
                await self.set_mode(dc.SET_CURRENT_OPERATING_MODE, {"relaunch": "on", "absence": "off"})

    async def set_temperature(self, temperature):
        """Set temperature."""
        if self.widget == dt.APC_WATER_HEATER:
            self.set_comfort_temperature(temperature)
        elif self.widget == dt.WATER_HEATER:
            await self.set_mode(dc.SET_TARGET_TEMP, temperature)

    async def set_eco_temperature(self, temperature):
        """Set operating mode."""
        await self.set_mode(dc.SET_ECO_TARGET_DHW_TEMPERATURE, temperature)

    async def set_comfort_temperature(self, temperature):
        """Set operating mode."""
        await self.set_mode(dc.SET_COMFORT_TARGET_DHW_TEMPERATURE, temperature)

    async def update(self):
        """Update water heater ."""
        if self.client is None:
            raise CozytouchException("Unable to update heater")
        for sensor in self.sensors:
            logger.debug("Water Heater : Update sensor")
            await sensor.update()
        await super(CozytouchWaterHeater, self).update()
