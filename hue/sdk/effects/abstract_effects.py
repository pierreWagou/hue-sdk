from typing import Generic, TypeVar, List
from abc import ABC

from pydantic import BaseModel

AbstractEffect = TypeVar("AbstractEffects")

class AbstractEffects(BaseModel, ABC, Generic[AbstractEffect]):

    status_values: List[AbstractEffect] | None = None
    status: AbstractEffect | None = None
    effect_values: List[AbstractEffect] | None = None