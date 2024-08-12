from dataclasses import dataclass

from hue.sdk.roomzone import RoomZone

@dataclass(kw_only=True)
class Room(RoomZone):

    type: str = "room"