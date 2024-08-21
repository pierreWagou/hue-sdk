from typing import Generic, TypeVar, ClassVar, Type
from abc import ABC

from hue.sdk.client.service.operator import ServiceOperator
from hue.sdk.client.session import HueSession
from hue.sdk.resource.resource_type import ResourceType

Resource = TypeVar("Resource")

class AbstractService(Generic[Resource], ABC):

    resource_cls: ClassVar[Type[Resource]]
    resource_type: ClassVar[ResourceType]
    operator: Type[ServiceOperator[Resource]] = ServiceOperator[Resource]


    def __init__(self, hue_session: HueSession):
        self.endpoint = self.resource_type.value
        self.hue_session = hue_session