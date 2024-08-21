from pydantic import BaseModel

from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.dimming import Dimming

class ColorTemperaturePalette(BaseModel):

    color_temperature: ColorTemperature
    dimming: Dimming

