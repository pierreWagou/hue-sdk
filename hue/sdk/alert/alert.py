from dataclasses import dataclass
from typing import List

from hue.sdk.alert.effect_type import AlertEffectType

@dataclass(kw_only=True)
class Alert:
    
    action_values = List[AlertEffectType]