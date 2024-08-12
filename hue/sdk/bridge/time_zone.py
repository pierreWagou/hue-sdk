from dataclasses import dataclass

@dataclass(kw_only=True)
class TimeZone:

    time_zone: str