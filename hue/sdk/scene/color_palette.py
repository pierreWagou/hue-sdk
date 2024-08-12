from dataclasses import dataclass

from hue.sdk.dimming import Dimming
from hue.sdk.color import Color

@dataclass(kw_only=True)
class ColorPalette:

    color: Color
    dimming: Dimming