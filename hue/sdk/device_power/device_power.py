from dataclasses import dataclass

from hue.sdk.device_power.power_state import PowerState
from hue.sdk.resource import Resource
from hue.sdk.resource_identifier.resource_identifier import ResourceIdentifier

@dataclass(kw_only=True)
class DevicePower(Resource):

    owner: ResourceIdentifier
    power_state: PowerState