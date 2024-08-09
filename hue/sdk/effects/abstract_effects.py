from dataclasses import dataclass
from typing import Generic, TypeVar, List
from abc import ABC

AbstractEffect = TypeVar("AbstractEffects")

@dataclass(kw_only=True)
class AbstractEffects(Generic[AbstractEffect], ABC):

    status_values: List[AbstractEffect]
    status: AbstractEffect
    effect_values: List[AbstractEffect]