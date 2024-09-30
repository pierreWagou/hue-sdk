from pydantic import BaseModel

from hue.sdk.color.xy import XY
from hue.sdk.color.gamut import Gamut
from hue.sdk.color.gamut_type import GamutType

class ColorPut(BaseModel):
    
    xy: XY | None = None