from enum import Enum
from logging import CRITICAL

class BatteryState(Enum):

    NORMAL = "normal"
    LOW = "low"
    CRITICAL = "critical"