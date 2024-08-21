from pydantic import BaseModel

from hue.sdk.device.device_status import DeviceStatus

class Usertest(BaseModel):
    status: DeviceStatus
    usertest: bool