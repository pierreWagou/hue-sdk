from typing import ClassVar, List, Type

from hue.sdk.client.service.abstract_service import AbstractService
from hue.sdk.dimming import Dimming
from hue.sdk.light import Light
from hue.sdk.on import On
from hue.sdk.identify import Identify
from hue.sdk.light.metadata import LightMetadata
from hue.sdk.resource.resource_type import ResourceType

class LightClient(AbstractService[Light]):

    resource_type: ClassVar[ResourceType] =  ResourceType.LIGHT
    resource_cls: ClassVar[Type[Light]] = Light

    def list(self) -> List[Light]:
        light_list = self.operator.list(
            hue_session=self.hue_session, 
            service_endpoint=self.endpoint, 
            resource_cls=self.resource_cls
        )
        return light_list
    
    def get(self, light_id: str) -> Light:
        light = self.operator.get(
            hue_session=self.hue_session, 
            service_endpoint=self.endpoint, 
            resource_id=light_id, 
            resource_cls=self.resource_cls
        )
        return light
    
    def update(
        self,
        light_id: str,
        type: ResourceType | None = None,
        metadata: LightMetadata | None = None,
        identify: Identify | None = None,
        on: On | None = None,
        dimming: Dimming | None = None,
        signaling: Signal | None = None
    ):
        self.operator.update(
            hue_session=self.hue_session, 
            service_endpoint=self.endpoint,
            resource_id=light_id,
            type=type,
            metadata=metadata,
            identify=identify,
            on=on,
            dimming=dimming
        )
