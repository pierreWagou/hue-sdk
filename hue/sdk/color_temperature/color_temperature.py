from pydantic import BaseModel

from hue.sdk.color_temperature.mirek_schema import MirekSchema

class ColorTemperature(BaseModel):
    
    mirek: int | None = None