from dataclasses import dataclass

from hue.sdk.dimming import Dimming
from hue.sdk.powerup.dimming.mode import DimmingMode

@dataclass(kw_only=True)
class PowerupDimming:

    mode: DimmingMode
    dimming: Dimming | None = None