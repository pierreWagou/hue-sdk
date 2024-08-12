from dataclasses import dataclass

from hue.sdk.resource_identifier.resource_type import ResourceType

@dataclass(kw_only=True)
class ResourceIdentifier:

    rid: str
    rtype: ResourceType