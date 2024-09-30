from hue.sdk.effects import Effects, TimedEffects
from hue.sdk.gradient import Gradient
from hue.sdk.identify import Identify
from hue.sdk.light.light import Light
from hue.sdk.light.metadata import LightMetadata
from hue.sdk.light.mode import Mode
from hue.sdk.powerup import Powerup
from hue.sdk.light.product_data import LightProductData
from hue.sdk.color_temperature import ColorTemperature, ColorTemperatureDelta
from hue.sdk.color import Color
from hue.sdk.dynamics import Dynamics
from hue.sdk.resource.resource_type import ResourceType

class LightGet(Light):

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
    identify: Identify | None = None    