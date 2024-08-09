from dataclasses import dataclass

from hue.sdk.effects.abstract_effects import AbstractEffects
from hue.sdk.effects.timed_effect import TimedEffect

@dataclass(kw_only=True)
class TimedEffects(AbstractEffects[TimedEffect]):
    pass