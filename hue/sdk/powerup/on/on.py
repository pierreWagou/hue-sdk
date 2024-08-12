from dataclasses import dataclass

from hue.sdk.on import On
from hue.sdk.powerup.on.mode import OnMode

@dataclass(kw_only=True)
class PowerupOn:
    
    mode: OnMode
    on: On | None = None