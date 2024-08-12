from dataclasses import dataclass
from typing import List

from hue.sdk.device.device_mode_value import DeviceModeValue
from hue.sdk.device.device_status import DeviceStatus

@dataclass(kw_only=True)
class DeviceMode:

    status: DeviceStatus
    mode: DeviceModeValue
    mode_values: List[DeviceModeValue]