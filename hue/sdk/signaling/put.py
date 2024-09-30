from dataclasses import dataclass
from typing import List

from hue.sdk.color.put import ColorPut
from hue.sdk.signaling.signal import Signal
from hue.sdk.signaling.signal_status import SignalStatus

@dataclass(kw_only=True)
class SignalingPut:

    signal: SignalStatus
    duration: int
    colors: List[ColorPut]