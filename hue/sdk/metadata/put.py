from pydantic import BaseModel

from hue.sdk.archetype import Archetype

class MetadataPut(BaseModel):

    name: str = None
    archetype: Archetype = None