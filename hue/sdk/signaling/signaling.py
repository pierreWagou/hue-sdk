from dataclasses import dataclass
from typing import List

from hue.sdk.signaling.signal import Signal
from hue.sdk.signaling.signal_status import SignalStatus

@dataclass(kw_only=True)
class Signaling:

    signal_values: List[Signal]
    status: SignalStatus | None = None