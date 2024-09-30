from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from hue.sdk.gradient.mode import GradientMode
from hue.sdk.gradient.point import GradientPoint

class GradientPut(BaseModel):

    points: List[GradientPoint]
    mode: GradientMode | None = None
    points_capable: int | None = None
    mode_values: List[GradientMode] | None = None
    pixel_count: int | None = None
