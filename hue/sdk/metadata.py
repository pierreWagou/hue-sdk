from pydantic import BaseModel

from hue.sdk.archetype import Archetype

class Metadata(BaseModel):

    name: str
    archetype: Archetype