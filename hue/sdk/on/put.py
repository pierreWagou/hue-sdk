from pydantic import BaseModel

class OnPut(BaseModel):
    
    on: bool = None