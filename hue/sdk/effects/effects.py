from dataclasses import dataclass

from hue.sdk.effects.abstract_effects import AbstractEffects
from hue.sdk.effects.effect import Effect

@dataclass(kw_only=True)
class Effects(AbstractEffects[Effect]):
    pass

