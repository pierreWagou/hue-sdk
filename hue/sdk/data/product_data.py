from dataclasses import dataclass

from hue.sdk.data.archetype import Archetype
from hue.sdk.data.function import Function

@dataclass(kw_only=True)
class ProductData:

    name: str | None = None
    archetype: Archetype | None = None
    function: Function