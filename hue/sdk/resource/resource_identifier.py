from pydantic import BaseModel

from hue.sdk.resource.resource_type import ResourceType

class ResourceIdentifier(BaseModel):

    rid: str
    rtype: ResourceType