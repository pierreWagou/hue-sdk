from hue.sdk.resource import ChildResource
from hue.sdk.bridge.time_zone import TimeZone
from hue.sdk.resource.resource_type import ResourceType

class Bridge(ChildResource):

    type: ResourceType = ResourceType.BRIDGE
    bridge_id: str
    time_zone: TimeZone

