from dataclasses import dataclass
from abc import ABC

from pydantic import BaseModel

from hue.sdk.alert.alert import Alert
from hue.sdk.dimming import Dimming, DimmingDelta
from hue.sdk.on import On
from hue.sdk.resource import ChildResource
from hue.sdk.signaling.signaling import Signaling

class AbstractLight(ABC, ChildResource):

    on: On | None = None
    dimming: Dimming | None = None
    dimming_delta: DimmingDelta | None = None
    alert: Alert | None = None
    signaling: Signaling | None = None