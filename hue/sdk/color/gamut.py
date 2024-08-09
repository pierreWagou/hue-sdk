from dataclasses import dataclass

from hue.sdk.color.xy import XY

@dataclass(kw_only=True)
class Gamut:
    red: XY
    green: XY
    blue: XY