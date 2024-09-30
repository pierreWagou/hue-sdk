from typing import List
from pydantic import BaseModel

from hue.sdk.dynamics.dynamic_status import DynamicStatus

class Dynamics(BaseModel):
    
    status: DynamicStatus | None = None
    status_values: List[DynamicStatus] | None = None
    duration: int | None = None
    speed: float
    speed_valid: bool | None = None