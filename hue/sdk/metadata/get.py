from pydantic import BaseModel

from hue.sdk.archetype import Archetype

class MetadataGet(BaseModel):

    name: str
    archetype: Archetype