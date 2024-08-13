from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

from hue.sdk.gradient.mode import GradientMode
from hue.sdk.gradient.point import GradientPoint

class Gradient(BaseModel):

    points: List[GradientPoint]
    mode: GradientMode
    points_capable: int
    mode_values: List[GradientMode]
    pixel_count: int | None = None
