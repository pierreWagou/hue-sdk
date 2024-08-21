from typing import List

from hue.sdk.device_software_update.problem import DeviceSoftwareUpdateProblem
from hue.sdk.resource import Resource
from hue.sdk.device_software_update.state import DeviceSofrwareUpdateState
from hue.sdk.resource.resource_type import ResourceType

class DeviceSoftwareUpdate(Resource):
    
    type: ResourceType = ResourceType.DEVICE_SOFTWARE_UPDATE
    state: DeviceSofrwareUpdateState
    problems: List[DeviceSoftwareUpdateProblem]
