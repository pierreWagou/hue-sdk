from typing import List
from pydantic import BaseModel

from hue.sdk.alert.effect_type import AlertEffectType

class AlertPut(BaseModel):
    
    action: AlertEffectType = AlertEffectType.BREATHE