from pydantic import BaseModel

class MirekSchema(BaseModel):
    
    mirek_minimum: int
    mirek_maximum: int