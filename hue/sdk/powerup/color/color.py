from pydantic import BaseModel

from hue.sdk.color import Color
from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.powerup.color.mode import ColorMode

class PowerupColor(BaseModel):

    mode: ColorMode
    color_temperature: ColorTemperature | None = None
    color: Color | None = None