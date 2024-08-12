from enum import Enum

class DeviceSofrwareUpdateState(Enum):
    
    NO_UPDATE = "no_update"
    UPDATE_PENDING = "update_pending"
    READY_TO_INSTALL = "ready_to_install"
    INSTALLING = "installing"