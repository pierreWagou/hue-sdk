from dataclasses import dataclass

from hue.sdk.archetype import Archetype

@dataclass(kw_only=True)
class DeviceProductData:

    model_id: str
    manufacturer_name: str
    product_name: str
    product_archetype: Archetype
    certified: bool
    software_version: str
    hardware_platform_type: str | None = None