from pydantic import BaseModel

from hue.sdk.powerup.color import PowerupColor
from hue.sdk.powerup.dimming import PowerupDimming
from hue.sdk.powerup.on import PowerupOn
from hue.sdk.powerup.preset import Preset

class Powerup(BaseModel):

    preset: Preset
    configured: bool
    on: PowerupOn
    dimming: PowerupDimming
    color: PowerupColor