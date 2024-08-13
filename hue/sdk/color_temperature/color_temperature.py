from pydantic import BaseModel

from hue.sdk.color_temperature.mirek_schema import MirekSchema

class ColorTemperature(BaseModel):
    
    mirek: int
    mirek_valid: bool | None = None
    mirek_schema: MirekSchema | None = None