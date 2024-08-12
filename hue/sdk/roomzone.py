from dataclasses import dataclass
from typing import List
from abc import ABC

from hue.sdk.resource import Resource
from hue.sdk.resource_identifier import ResourceIdentifier
from hue.sdk.data.metadata import Metadata

@dataclass(kw_only=True)
class RoomZone(ABC, Resource):

    type: str
    children: List[ResourceIdentifier]
    services: List[ResourceIdentifier]
    metadata: Metadata