from pydantic import BaseModel

from hue.sdk.color import Color

class GradientPoint(BaseModel):

    color: Color