from typing import ClassVar, List, Type

from hue.sdk.client.service.abstract_service import AbstractService
from hue.sdk.light import Light
from hue.sdk.light.light_put import LightPut
from hue.sdk.light.light_get import LightGet
from hue.sdk.resource.resource_type import ResourceType

class LightClient(AbstractService[Light]):

    resource_type: ClassVar[ResourceType] =  ResourceType.LIGHT
    resource_cls: ClassVar[Type[Light]] = Light

    def list(self) -> List[Light]:
        light_list = self.operator.list(
            hue_session=self.hue_session, 
            service_endpoint=self.endpoint, 
            resource_cls=LightGet
        )
        return light_list
    
    def get(self, light_id: str) -> Light:
        light = self.operator.get(
            hue_session=self.hue_session, 
            service_endpoint=self.endpoint, 
            resource_id=light_id, 
            resource_cls=LightGet
        )
        return light
    
    def update(
        self,
        light_id: str,
        light: LightPut
    ):
        self.operator.update(
            hue_session=self.hue_session, 
            service_endpoint=self.endpoint,
            resource_id=light_id,
            resource = light,
        )
