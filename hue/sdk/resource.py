from dataclasses import dataclass

@dataclass(kw_only=True)
class Resource:

    type: str
    id: str
    id_v1: str | None = None