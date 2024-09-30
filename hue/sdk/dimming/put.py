from pydantic import BaseModel

class DimmingPut(BaseModel):
    
    brightness: float | None = None