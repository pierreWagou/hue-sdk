from typing import Generic, TypeVar, List
from abc import ABC

from pydantic import BaseModel

AbstractEffect = TypeVar("AbstractEffects")

class AbstractEffects(BaseModel, Generic[AbstractEffect], ABC):

    status_values: List[AbstractEffect]
    status: AbstractEffect
    effect_values: List[AbstractEffect]