from dataclasses import dataclass
from typing import List

from hue.sdk.resource import Resource
from hue.sdk.resource.resource_identifier import ResourceIdentifier

@dataclass(kw_only=True)
class ParentResource(Resource):

    children: List[ResourceIdentifier]
    services: List[ResourceIdentifier]