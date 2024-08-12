from dataclasses import dataclass
from typing import List

from hue.sdk.resource import Resource
from hue.sdk.resource_identifier import ResourceIdentifier

@dataclass(kw_only=True)
class BridgeHome(Resource):

    type: str = "bridge_home"
    children: List[ResourceIdentifier]
    services: List[ResourceIdentifier]