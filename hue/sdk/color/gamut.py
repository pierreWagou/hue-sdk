from pydantic import BaseModel

from hue.sdk.color.xy import XY

class Gamut(BaseModel):
    red: XY
    green: XY
    blue: XY