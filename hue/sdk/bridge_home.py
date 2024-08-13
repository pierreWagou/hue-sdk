from typing import List

from pydantic import BaseModel

from hue.sdk.resource import ParentResource
from hue.sdk.resource.resource_identifier import ResourceIdentifier
from hue.sdk.resource.resource_type import ResourceType

class BridgeHome(BaseModel, ParentResource):

    type: str = ResourceType.BRIDGE_HOME
    children: List[ResourceIdentifier]
    services: List[ResourceIdentifier]