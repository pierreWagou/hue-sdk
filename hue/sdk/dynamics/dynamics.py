from typing import List
from pydantic import BaseModel

from hue.sdk.dynamics.dynamic_status import DynamicStatus

class Dynamics(BaseModel):
    
    status: DynamicStatus
    status_values: List[DynamicStatus]
    speed: float
    speed_valid: bool