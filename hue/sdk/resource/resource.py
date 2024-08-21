from pydantic import BaseModel

from hue.sdk.resource.resource_type import ResourceType

class Resource(BaseModel):

    type: ResourceType
    id: str
    id_v1: str | None = None