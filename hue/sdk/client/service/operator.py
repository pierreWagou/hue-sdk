from enum import Enum
import json
from typing import Generic, TypeVar, Type, List, Any

from pydantic import BaseModel

from hue.sdk.client.session import HueSession

Resource = TypeVar("Resource")

class ServiceOperator(Generic[Resource]):

    @staticmethod
    def list(hue_session: HueSession, service_endpoint: str, resource_cls: Resource) -> List[Resource]:
        resource_list_data = hue_session.get(url=service_endpoint)
        resource_list = [resource_cls.model_validate(resource_data) for resource_data in resource_list_data]
        return resource_list

    @staticmethod
    def get(hue_session: HueSession, service_endpoint: str, resource_cls: Type[Resource], resource_id: str) -> Resource:
        url = f"{service_endpoint}/{resource_id}"
        resource_data = hue_session.get(url=url)[0]
        resource = resource_cls.model_validate(resource_data)
        return resource
    
    @staticmethod
    def create(hue_session: HueSession, service_endpoint: str, resource: Resource):
        hue_session.post(url=service_endpoint, json=resource.dict())
    
    @classmethod
    def serialize(cls, obj: Any) -> Any:
        if isinstance(obj, Enum):
            value = obj.value
        elif isinstance(obj, BaseModel):
            value_json = obj.model_dump_json(exclude_none=True)
            value = json.loads(value_json)
        else:
            value = obj
        return value

    @classmethod
    def update(cls, hue_session: HueSession, service_endpoint: str, resource_id: str, **kwargs):
        url = f"{service_endpoint}/{resource_id}"
        json_data = {key: cls.serialize(obj=value) for key, value in kwargs.items() if value}
        hue_session.put(url=url, json=json_data)
    
    @staticmethod
    def delete(self, resource_id: str):
        self.hue_session.delete(url=resource_id)