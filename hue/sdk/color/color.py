from dataclasses import dataclass

from hue.sdk.color.xy import XY
from hue.sdk.color.gamut import Gamut
from hue.sdk.color.gamut_type import GamutType

@dataclass(kw_only=True)
class Color:
    xy: XY
    gamut: Gamut | None = None
    gamut_type: GamutType | None = None