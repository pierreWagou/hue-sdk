from pydantic import BaseModel

from hue.sdk.metadata import Metadata
from hue.sdk.resource import ParentResource
from hue.sdk.resource.resource_type import ResourceType

class Room(BaseModel, ParentResource):

    type: ResourceType = ResourceType.ROOM
    metadata: Metadata