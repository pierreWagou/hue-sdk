from enum import Enum

class Preset(Enum):

    SAFETY = "safety"
    POWERFAIL = "powerfail"
    LAST_ON_STATE = "last_on_state"
    CUSTOM = "custom"