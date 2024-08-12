from dataclasses import dataclass

from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.dimming import Dimming

@dataclass(kw_only=True)
class ColorTemperaturePalette:

    color_temperature: ColorTemperature
    dimming: Dimming

