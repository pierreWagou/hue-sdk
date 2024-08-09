from dataclasses import dataclass

from hue.sdk.color import Color

@dataclass(kw_only=True)
class GradientPoint:

    color: Color