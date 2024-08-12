from dataclasses import dataclass

from hue.sdk.device_power.battery_state import BatteryState

@dataclass(kw_only=True)
class PowerState:
    
    battery_state: BatteryState | None = None
    battery_level: int | None = None