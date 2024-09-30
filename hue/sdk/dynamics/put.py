from typing import List
from pydantic import BaseModel

from hue.sdk.dynamics.dynamic_status import DynamicStatus

class DynamicsPut(BaseModel):
    
    duration: int | None = None
    speed: float | None = None