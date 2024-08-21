from typing import ClassVar
import requests
from requests import Session

from hue.sdk.client.token import HueToken, HueTokenFactory

class HueSession(Session):

    host: ClassVar[str] = "https://api.meethue.com"

    def __init__(self, client_id: str, client_secret: str, code: str | None = None, hue_token: HueToken | None = None):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        token_url = f"{self.host}/v2/oauth2/token"
        self.hue_token_factory = HueTokenFactory(token_url=token_url)
        self.hue_token = self.hue_token_factory.build(client_id=client_id, client_secret=client_secret, code=code, hue_token=hue_token)
        self.username = self.get_username(access_token=self.hue_token.access_token)
        self.set_headers()
    
    def set_headers(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.hue_token.access_token}",
            "hue-application-key": self.username
        }
    
    @property
    def route_url(self) -> str:
        route_url = f"{self.host}/route"
        return route_url

    @property
    def api_url(self) -> str:
        api_url = f"{self.route_url}/clip/v2/resource"
        return api_url
    
    def get_username(self, access_token: str) -> str:
        route_api_url = f"{self.route_url}/api"
        config_url = f"{route_api_url}/0/config"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        data = {
            "linkbutton": True
        }
        requests.put(url=config_url, headers=headers, json=data)
        data = {
            "devicetype": "wagou"
        }
        response = requests.post(url=route_api_url, headers=headers, json=data)
        username = response.json()[0]["success"]["username"]
        return username

    def renew_token(self):
        self.hue_token = self.hue_token_factory.renew_hue_token(client_id=self.client_id, client_secret=self.client_secret, hue_token=self.hue_token)
        self.set_headers()
    
    def request(self, method, url, **kwargs):
        self.renew_token()
        full_url = f"{self.api_url}/{url}"
        response = super().request(method, full_url, **kwargs)
        if response.status_code // 100 != 2:
            print(response.text)
            response.raise_for_status()
        response_json = response.json()
        data = response_json["data"]
        return data