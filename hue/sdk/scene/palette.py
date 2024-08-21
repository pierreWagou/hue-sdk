from typing import List
from pydantic import BaseModel

from hue.sdk.dimming import Dimming
from hue.sdk.scene.color_palette import ColorPalette
from hue.sdk.scene.color_temperature_palette import ColorTemperaturePalette
from hue.sdk.effects import Effects

class Palette(BaseModel):
    
    color: List[ColorPalette] | None = None
    dimming: List[Dimming]
    color_temperature: List[ColorTemperaturePalette]
    effects: List[Effects]
