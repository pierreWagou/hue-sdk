from pydantic import BaseModel

class Dimming(BaseModel):
    
    brightness: float
    min_dim_level: float | None = None