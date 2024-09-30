from pydantic import BaseModel

class DimmingGet(BaseModel):
    
    brightness: float
    min_dim_level: float | None = None