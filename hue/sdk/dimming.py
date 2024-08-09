from dataclasses import dataclass

@dataclass(kw_only=True)
class Dimming:
    
    brightness: float
    min_dim_level: float | None = None