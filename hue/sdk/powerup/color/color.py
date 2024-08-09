from dataclasses import dataclass

from hue.sdk.color import Color
from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.powerup.color.mode import ColorMode

@dataclass(kw_only=True)
class PowerupColor:

    mode: ColorMode
    color_temperature: ColorTemperature | None = None
    color: Color | None = None