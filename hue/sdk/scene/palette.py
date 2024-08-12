from dataclasses import dataclass
from typing import List

from hue.sdk.dimming import Dimming
from hue.sdk.scene.color_palette import ColorPalette
from hue.sdk.scene.color_temperature_palette import ColorTemperaturePalette
from hue.sdk.effects import Effects

@dataclass(kw_only=True)
class Palette:
    
    color: List[ColorPalette] | None = None
    dimming: List[Dimming]
    color_temperature: List[ColorTemperaturePalette]
    effects: List[Effects]
