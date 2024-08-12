from dataclasses import dataclass

from hue.sdk.roomzone import RoomZone

@dataclass(kw_only=True)
class Zone(RoomZone):

    type: str = "zone"