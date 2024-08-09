from dataclasses import dataclass

from hue.sdk.data.archetype import Archetype
from hue.sdk.data.function import Function

@dataclass(kw_only=True)
class Metadata:

    name: str
    archetype: Archetype
    fixed_mired: int | None = None
    function: Function