from abc import ABC
from typing import ClassVar, Generic, List, TypeVar

from hue.sdk.client.token import HueToken
from hue.sdk.client.session import HueSession
from hue.sdk.client.service.light_service import LightClient

class HueClient:

    def __init__(self, client_id: str, client_secret: str, code: str | None = None, hue_token: HueToken | None = None):
        self.hue_session = HueSession(
            client_id=client_id, 
            client_secret=client_secret, 
            code=code, 
            hue_token=hue_token,
        )
        self.light = LightClient(hue_session=self.hue_session)

