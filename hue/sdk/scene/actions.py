from dataclasses import dataclass

from hue.sdk.scene.action import Action
from hue.sdk.resource_identifier import ResourceIdentifier

@dataclass(kw_only=True)
class Actions:

    target: ResourceIdentifier
    action: Action