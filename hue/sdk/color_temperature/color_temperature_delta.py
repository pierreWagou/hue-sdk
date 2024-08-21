from pydantic import BaseModel

from hue.sdk.delta_action import DeltaAction

class ColorTemperatureDelta(BaseModel):

    action: DeltaAction
    brightness_delta: float | None = None