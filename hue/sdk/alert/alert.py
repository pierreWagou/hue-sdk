from typing import List
from pydantic import BaseModel

from hue.sdk.alert.effect_type import AlertEffectType

class Alert(BaseModel):
    
    action_values: List[AlertEffectType] | None = None
    action: AlertEffectType | None = None