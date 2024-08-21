from pydantic import BaseModel

from hue.sdk.scene.action import Action
from hue.sdk.resource.resource_identifier import ResourceIdentifier

class Actions(BaseModel):

    target: ResourceIdentifier
    action: Action