from dataclasses import dataclass

from hue.sdk.owner.ressource_type import ResourceType

@dataclass(kw_only=True)
class Owner:

    rid: str
    rtype: ResourceType