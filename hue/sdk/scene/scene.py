from dataclasses import dataclass
from typing import List

from hue.sdk.resource.resource import Resource
from hue.sdk.scene.action import Action
from hue.sdk.scene.palette import Palette
from hue.sdk.resource.resource_identifier import ResourceIdentifier
from hue.sdk.resource.resource_type import ResourceType
from hue.sdk.scene.scene_metadata import SceneMetadata
from hue.sdk.scene.scene_status import SceneStatus

class Scene(Resource):

    type: ResourceType = ResourceType.SCENE
    id: str
    id_v1: str | None = None
    actions: List[Action]
    palette: Palette
    metadata: SceneMetadata
    group: ResourceIdentifier
    speed: float
    auto_dynamic: bool
    status: SceneStatus