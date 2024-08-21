from pydantic import BaseModel

from hue.sdk.dimming import Dimming
from hue.sdk.color import Color

class ColorPalette(BaseModel):

    color: Color
    dimming: Dimming