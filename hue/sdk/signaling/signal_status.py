from dataclasses import dataclass
from typing import List
from datetime import datetime

from hue.sdk.signaling.signal import Signal
from hue.sdk.color import Color


@dataclass(kw_only=True)
class SignalStatus:
    
    signal: Signal
    estimated_end: datetime
    colors: List[Color]