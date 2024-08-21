from dataclasses import dataclass

from hue.sdk.device.device_product_data import DeviceProductData
from hue.sdk.metadata import Metadata
from hue.sdk.device.device_mode import DeviceMode
from hue.sdk.resource import Resource
from hue.sdk.device.usertest import Usertest
from hue.sdk.resource.resource_identifier import ResourceIdentifier
from hue.sdk.resource.resource_type import ResourceType

class Device(Resource):

    type: ResourceType = ResourceType.DEVICE
    product_data: DeviceProductData
    metadata: Metadata
    usertest: Usertest | None = None
    device_mode: DeviceMode | None = None
    services: ResourceIdentifier
