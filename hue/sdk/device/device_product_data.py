from pydantic import BaseModel

from hue.sdk.archetype import Archetype

class DeviceProductData(BaseModel):

    model_id: str
    manufacturer_name: str
    product_name: str
    product_archetype: Archetype
    certified: bool
    software_version: str
    hardware_platform_type: str | None = None