from dataclasses import dataclass

@dataclass(kw_only=True)
class XY:
    x: float
    y: float