from typing import List
from pydantic import BaseModel

from hue.sdk.device.device_mode_value import DeviceModeValue
from hue.sdk.device.device_status import DeviceStatus

class DeviceMode(BaseModel):

    status: DeviceStatus
    mode: DeviceModeValue
    mode_values: List[DeviceModeValue]