import requests
import datetime

from typing import Optional

from youless_api.const import STATE_OK, STATE_FAILED
from youless_api.youless_sensor import YoulessSensor, PowerMeter, DeliveryMeter, ExtraMeter


def validate_enologic_response(raw_data: dict) -> dict:
    """Validate the response to verify that it makes sense and no junk data is returned"""

    corrected = {**{'p1': None, 'p2': None, 'n1': None, 'n2': None, 'gas': None}, **raw_data}
    if 'gts' in corrected:
        formatted_date = datetime.datetime.now().strftime("%y%m%d") + "0000"
        if corrected["gts"] != 0 and int(formatted_date) >= corrected["gts"]:
            corrected["gas"] = None

    return corrected


def validate_basic_response(raw_data: dict) -> dict:
    """Validate the response from the old /a interface and adjust the dict if needed."""

    corrected = {**{'cs0': None, 'ps0': None}, **raw_data}
    parse_float_values_for = ['cnt', 'cs0']

    for correct_value in parse_float_values_for:
        if correct_value in corrected and corrected[correct_value] is not None:
            corrected[correct_value] = float(corrected[correct_value].replace(",", "."))

    return corrected


class YouLessDevice:
    """The base class for the Youless devices"""

    def __init__(self):
        """Initialize the state"""

    @property
    def state(self) -> Optional[str]:
        """The current state of the connection"""
        return None

    @property
    def error(self) -> Optional[str]:
        """Returns the last known error, only if state == 'FAILED'"""
        return None

    @property
    def mac_address(self) -> Optional[str]:
        """Returns the MAC address"""
        return None

    @property
    def model(self) -> Optional[str]:
        """Returns the model number of the device"""
        return None

    @property
    def gas_meter(self) -> Optional[YoulessSensor]:
        """"Get the gas data available."""
        return None

    @property
    def current_power_usage(self) -> Optional[YoulessSensor]:
        """Get the current power usage."""
        return None

    @property
    def power_meter(self) -> Optional[PowerMeter]:
        """Get the power meter values."""
        return None

    @property
    def delivery_meter(self) -> Optional[DeliveryMeter]:
        """Get the power delivered values."""
        return None

    @property
    def extra_meter(self) -> Optional[ExtraMeter]:
        """Get the meter values of an attached meter."""
        return None

    def update(self) -> None:
        """Placeholder to update values from device"""


class LS120(YouLessDevice):
    """The device integration for the Youless LS120"""

    def __init__(self, host, device_information):
        """Initialize the integration"""
        super().__init__()
        self._host = host
        self._cache = None
        self._state = STATE_OK
        self._info = device_information

    @property
    def gas_meter(self):
        """"Get the gas meter from the internal cache"""
        if self._cache is not None:
            return YoulessSensor(self._cache['gas'], 'm3')

        return None

    @property
    def current_power_usage(self):
        """Get the current power usage from the internal cache"""
        if self._cache is not None:
            return YoulessSensor(self._cache['pwr'], 'W')

        return None

    @property
    def power_meter(self):
        """Get the power meter values."""
        if self._cache is not None:
            return PowerMeter(
                YoulessSensor(self._cache['p1'], 'kWh'),
                YoulessSensor(self._cache['p2'], 'kWh'),
                YoulessSensor(self._cache['net'], 'kWh')
            )

        return None

    @property
    def delivery_meter(self):
        """Get the power delivered values."""
        if self._cache is not None:
            return DeliveryMeter(
                YoulessSensor(self._cache['n1'], 'kWh'),
                YoulessSensor(self._cache['n2'], 'kWh')
            )

        return None

    @property
    def extra_meter(self):
        """Get the meter values of an attached meter."""
        if self._cache is not None:
            return ExtraMeter(
                YoulessSensor(self._cache['cs0'], 'kWh'),
                YoulessSensor(self._cache['ps0'], 'W')
            )

        return None

    @property
    def state(self) -> Optional[str]:
        """Returns the current connectivity state"""
        return self._state

    @property
    def mac_address(self) -> Optional[str]:
        """Return the MAC address"""
        if self._info is not None:
            return self._info['mac']

        return None

    @property
    def model(self) -> Optional[str]:
        """Return the device model"""
        return "LS120"

    def update(self) -> None:
        """Update the sensor values from the device"""
        response = requests.get(f"{self._host}/e", timeout=2)
        if response.ok:
            response = validate_enologic_response(response.json()[0])
            if response is not None:
                self._state = STATE_OK
                self._cache = response
            else:
                self._state = STATE_FAILED
        else:
            self._state = STATE_FAILED


class LS110(YouLessDevice):
    """The device integration for the Youless LS110"""

    def __init__(self, host):
        """Initialize the integration"""
        super().__init__()
        self._host = host
        self._cache = None
        self._state = STATE_OK

    @property
    def state(self) -> Optional[str]:
        """Get the current device connectivity state"""
        return self._state

    @property
    def model(self) -> Optional[str]:
        """Return the device model"""
        return "LS110"

    @property
    def power_meter(self) -> Optional[PowerMeter]:
        """Fetch the power meter values from the internal cache"""
        if self._cache is not None:
            return PowerMeter(
                YoulessSensor(None, None),
                YoulessSensor(None, None),
                YoulessSensor(self._cache['cnt'], 'kWh')
            )

        return None

    @property
    def current_power_usage(self) -> Optional[YoulessSensor]:
        """Fetch the current power usage from the internal cache"""
        if self._cache is not None:
            return YoulessSensor(self._cache['pwr'], 'W')

        return None

    @property
    def extra_meter(self):
        """Get the meter values of an attached meter."""
        if self._cache is not None:
            return ExtraMeter(
                YoulessSensor(self._cache['cs0'], 'kWh'),
                YoulessSensor(self._cache['ps0'], 'W')
            )

        return None

    def update(self) -> None:
        """Update the sensor values from the device"""
        response = requests.get(f"{self._host}/a?f=j", timeout=2)
        if response.ok:
            validated_response = validate_basic_response(response.json())
            self._state = STATE_OK
            self._cache = validated_response
        else:
            self._state = STATE_FAILED


class LS120PVOutput(LS110):

    def __init__(self, host, device_information):
        super(LS120PVOutput, self).__init__(host)
        self._info = device_information

    @property
    def model(self) -> Optional[str]:
        return "LS120 - PVOutput"

    @property
    def mac_address(self) -> Optional[str]:
        """Return the MAC address"""
        if self._info is not None:
            return self._info['mac']

        return None
