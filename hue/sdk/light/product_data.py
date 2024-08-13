from pydantic import BaseModel

from hue.sdk.archetype import Archetype
from hue.sdk.light.function import Function

class LightProductData(BaseModel):

    name: str | None = None
    archetype: Archetype | None = None
    function: Function