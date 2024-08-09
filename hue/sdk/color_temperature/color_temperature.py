from dataclasses import dataclass

from hue.sdk.color_temperature.mirek_schema import MirekSchema

@dataclass(kw_only=True)
class ColorTemperature:
    
    mirek: int
    mirek_valid: bool
    mirek_schema: MirekSchema