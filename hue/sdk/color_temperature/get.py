from hue.sdk.color_temperature import ColorTemperature
from hue.sdk.color_temperature.mirek_schema import MirekSchema

class ColorTemperatureGet(ColorTemperature):
    
    mirek: int
    mirek_valid: bool | None = None
    mirek_schema: MirekSchema | None = None