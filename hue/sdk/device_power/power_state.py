from pydantic import BaseModel

from hue.sdk.device_power.battery_state import BatteryState

class PowerState(BaseModel):
    
    battery_state: BatteryState | None = None
    battery_level: int | None = None