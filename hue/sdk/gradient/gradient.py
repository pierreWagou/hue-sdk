from dataclasses import dataclass
from typing import List

from hue.sdk.gradient.mode import GradientMode
from hue.sdk.gradient.point import GradientPoint

@dataclass(kw_only=True)
class Gradient:

    points: List[GradientPoint]
    mode: GradientMode
    points_capable: int
    mode_values: List[GradientMode]
    pixel_count: int | None = None
