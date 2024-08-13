from pydantic import BaseModel

from hue.sdk.on import On
from hue.sdk.powerup.on.mode import OnMode

class PowerupOn(BaseModel):
    
    mode: OnMode
    on: On | None = None