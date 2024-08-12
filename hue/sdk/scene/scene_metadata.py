from dataclasses import dataclass

from hue.sdk.resource_identifier.resource_identifier import ResourceIdentifier

@dataclass(kw_only=True)
class SceneMetadata:
    
    name: str
    image: ResourceIdentifier | None = None
    appdata: str | None = None