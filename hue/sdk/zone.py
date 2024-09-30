from hue.sdk.metadata.get import Metadata
from hue.sdk.resource import ParentResource
from hue.sdk.resource.resource_type import ResourceType

class Zone(ParentResource):

    type: ResourceType = ResourceType.ZONE
    mdetadata: Metadata