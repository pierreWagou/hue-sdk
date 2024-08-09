from dataclasses import dataclass

@dataclass(kw_only=True)
class MirekSchema:
    
    mirek_minimum: int
    mirek_maximum: int