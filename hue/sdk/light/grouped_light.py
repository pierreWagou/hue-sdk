from pydantic import BaseModel

from hue.sdk.light.abstract_light import AbstractLight
from hue.sdk.resource.resource_type import ResourceType

class GroupedLight(BaseModel, AbstractLight):

    type: ResourceType = ResourceType.GROUPED_LIGHT