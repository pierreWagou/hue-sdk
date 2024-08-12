from dataclasses import dataclass
from typing import ClassVar

from hue.sdk.effects import Effects, TimedEffects
from hue.sdk.gradient import Gradient
from hue.sdk.light.abstract_light import AbstractLight
from hue.sdk.light.mode import Mode
from hue.sdk.data.metadata import Metadata
from hue.sdk.powerup import Powerup
from hue.sdk.data.light_product_data import LightProductData
from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.color import Color
from hue.sdk.dynamics import Dynamics

@dataclass(kw_only=True)
class Light(AbstractLight):

    type: str = "light"
    metadata: Metadata
    product_data: LightProductData | None = None
    service_id: int
    color_temperature: ColorTemperature | None = None
    color: Color | None = None
    dynamics: Dynamics | None = None
    mode: Mode
    gradient: Gradient | None = None
    effects: Effects | None = None
    timed_effects: TimedEffects | None = None
    powerup: Powerup | None = None
