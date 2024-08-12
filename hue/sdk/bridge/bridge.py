from dataclasses import dataclass

from hue.sdk.resource import Resource
from hue.sdk.resource_identifier import ResourceIdentifier
from hue.sdk.bridge.time_zone import TimeZone

@dataclass(kw_only=True)
class Bridge(Resource):

    type: str = "bridge"
    owner: ResourceIdentifier
    bridge_id: str
    time_zone: TimeZone

