from dataclasses import dataclass
from abc import ABC

from hue.sdk.alert.alert import Alert
from hue.sdk.dimming import Dimming
from hue.sdk.on import On
from hue.sdk.resource import ChildResource
from hue.sdk.signaling.signaling import Signaling

@dataclass(kw_only=True)
class AbstractLight(ABC, ChildResource):

    on: On | None = None
    dimming: Dimming | None = None
    alert: Alert | None = None
    signaling: Signaling | None = None