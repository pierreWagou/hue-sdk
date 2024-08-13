from dataclasses import dataclass

from hue.sdk.resource.resource_type import ResourceType

@dataclass(kw_only=True)
class Resource:

    type: ResourceType
    id: str
    id_v1: str | None = None