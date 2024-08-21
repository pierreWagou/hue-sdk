from hue.sdk.light.abstract_light import AbstractLight
from hue.sdk.resource.resource_type import ResourceType

class GroupedLight(AbstractLight):

    type: ResourceType = ResourceType.GROUPED_LIGHT