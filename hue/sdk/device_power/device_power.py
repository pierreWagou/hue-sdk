from hue.sdk.device_power.power_state import PowerState
from hue.sdk.resource import Resource
from hue.sdk.resource.child_resource import ChildResource
from hue.sdk.resource.resource_type import ResourceType

class DevicePower(ChildResource):

    type: ResourceType = ResourceType.DEVICE_POWER
    power_state: PowerState