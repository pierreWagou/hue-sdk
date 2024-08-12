from dataclasses import dataclass

from hue.sdk.light.abstract_light import AbstractLight

@dataclass(kw_only=True)
class GroupedLight(AbstractLight):

    type: str = "grouped_light"