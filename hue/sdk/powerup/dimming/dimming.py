from pydantic import BaseModel

from hue.sdk.dimming import Dimming
from hue.sdk.powerup.dimming.mode import DimmingMode

class PowerupDimming(BaseModel):

    mode: DimmingMode
    dimming: Dimming | None = None