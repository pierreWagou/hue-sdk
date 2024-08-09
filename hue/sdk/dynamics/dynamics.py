from dataclasses import dataclass
from typing import List

from hue.sdk.dynamics.dynamic_status import DynamicStatus

@dataclass(kw_only=True)
class Dynamics:
    
    status: DynamicStatus
    status_values: List[DynamicStatus]
    speed: float
    speed_valid: bool