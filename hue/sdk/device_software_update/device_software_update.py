from dataclasses import dataclass

from hue.sdk.device_software_update.problem import DeviceSoftwareUpdateProblem
from hue.sdk.resource import Resource
from hue.sdk.device_software_update.state import DeviceSofrwareUpdateState

@dataclass(kw_only=True)
class DeviceSoftwareUpdate(Resource):
    
    type: str = "device_software_update"
    state: DeviceSofrwareUpdateState
    problems: List[DeviceSoftwareUpdateProblem]
