from hue.sdk.alert.put import AlertPut
from hue.sdk.color.put import ColorPut
from hue.sdk.color_temperature.put import ColorTemperaturePut
from hue.sdk.dimming.put import DimmingPut
from hue.sdk.dynamics.put import DynamicsPut
from hue.sdk.identify import Identify
from hue.sdk.light.light import Light

from hue.sdk.color_temperature import ColorTemperatureDelta
from hue.sdk.dimming import DimmingDelta
from hue.sdk.metadata.put import MetadataPut
from hue.sdk.on.put import OnPut
from hue.sdk.signaling.put import SignalingPut

class LightPut(Light):

    type: ResourceType = ResourceType.LIGHT
    metadata: MetadataPut | None = None
    identify: Identify | None = None
    on: OnPut | None = None
    dimming: DimmingPut | None = None
    dimming_delta: DimmingDelta | None = None
    color_temperature: ColorTemperaturePut | None = None
    color_temperature_delta: ColorTemperatureDelta | None = None
    color: ColorPut | None = None
    dynamics: DynamicsPut | None = None
    alert: AlertPut | None = None
    signaling: SignalingPut | None = None
    gradient: 
