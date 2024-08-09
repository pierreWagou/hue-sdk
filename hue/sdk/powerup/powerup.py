from dataclasses import dataclass

from hue.sdk.powerup.color import PowerupColor
from hue.sdk.powerup.dimming import PowerupDimming
from hue.sdk.powerup.on import PowerupOn
from hue.sdk.powerup.preset import Preset

@dataclass(kw_only=True)
class Powerup:

    preset: Preset
    configured: bool
    on: PowerupOn
    dimming: PowerupDimming
    color: PowerupColor