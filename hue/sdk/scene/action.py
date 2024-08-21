from pydantic import BaseModel

from hue.sdk.dynamics import Dynamics
from hue.sdk.effects import Effects
from hue.sdk.gradient import Gradient
from hue.sdk.color import Color
from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.dimming import Dimming
from hue.sdk.on import On

class Action(BaseModel):

    on: On | None = None
    dimmming:  Dimming | None = None
    color: Color | None = None
    color_temperature: ColorTemperature | None = None
    gradient: Gradient | None = None
    effects: Effects | None = None
    dynamics: Dynamics | None = None