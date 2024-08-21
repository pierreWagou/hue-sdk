from pydantic import BaseModel

from hue.sdk.resource.resource_identifier import ResourceIdentifier

class SceneMetadata(BaseModel):
    
    name: str
    image: ResourceIdentifier | None = None
    appdata: str | None = None