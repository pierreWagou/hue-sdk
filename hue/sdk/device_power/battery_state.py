from enum import Enum

class BatteryState(Enum):

    NORMAL = "normal"
    LOW = "low"
    CRITICAL = "critical"