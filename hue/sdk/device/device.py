from dataclasses import dataclass

from hue.sdk.data.device_product_data import DeviceProductData
from hue.sdk.data.metadata import Metadata
from hue.sdk.device.device_mode import DeviceMode
from hue.sdk.resource import Resource
from hue.sdk.resource_identifier.resource_identifier import ResourceIdentifier
from hue.sdk.device.usertest import Usertest

@dataclass(kw_only=True)
class Device(Resource):

    type: str = "device"
    product_data: DeviceProductData
    metadata: Metadata
    usertest: Usertest | None = None
    device_mode: DeviceMode | None = None
    services: ResourceIdentifier
