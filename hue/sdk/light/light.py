from dataclasses import dataclass
from typing import ClassVar

from hue.sdk.effects import Effects, TimedEffects
from hue.sdk.gradient import Gradient
from hue.sdk.light.mode import Mode
from hue.sdk.owner.owner import Owner
from hue.sdk.data.metadata import Metadata
from hue.sdk.powerup import Powerup
from hue.sdk.data.product_data import ProductData
from hue.sdk.light.on import On
from hue.sdk.dimming import Dimming
from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.color import Color
from hue.sdk.dynamics import Dynamics
from hue.sdk.alert import Alert
from hue.sdk.signaling import Signaling

@dataclass(kw_only=True)
class Light:

    type: ClassVar[str] = "light"

    id: str
    id_v1: str | None = None
    owner: Owner
    metadata: Metadata
    product_data: ProductData | None = None
    service_id: int
    on: On
    dimming: Dimming | None = None
    color_temperature: ColorTemperature | None = None
    color: Color | None = None
    dynamics: Dynamics | None = None
    alert: Alert | None = None
    signaling: Signaling | None = None
    mode: Mode
    gradient: Gradient | None = None
    effects: Effects | None = None
    timed_effects: TimedEffects | None = None
    powerup: Powerup | None = None
