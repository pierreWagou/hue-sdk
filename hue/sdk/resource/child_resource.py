from dataclasses import dataclass

from hue.sdk.resource import Resource
from hue.sdk.resource.resource_identifier import ResourceIdentifier

@dataclass(kw_only=True)
class ChildResource(Resource):

    owner: ResourceIdentifier