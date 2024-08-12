from dataclasses import dataclass

from hue.sdk.device.device_status import DeviceStatus

@dataclass(kw_only=True)
class Usertest:
    status: DeviceStatus
    usertest: bool