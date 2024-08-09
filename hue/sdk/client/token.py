from dataclasses import dataclass
from typing import Dict
import time
import requests
from requests.auth import HTTPDigestAuth

import keyring

@dataclass(kw_only=True)
class HueToken:

    access_token: str
    expires_at: int
    refresh_token: str
    token_type: str = "bearer"
    
    @property
    def is_expired(self) -> bool:
        return self.expires_at < time.time()

@dataclass(kw_only=True)
class HueTokenFactory:

    token_url: str

    def request_hue_token(self, client_id: str, client_secret: str, code: str) -> HueToken:
        data = {
            "grant_type": "authorization_code",
            "code": code
        }
        hue_token = self.get_hue_token(client_id=client_id, client_secret=client_secret, data=data)
        return hue_token
    
    def refresh_hue_token(self, client_id: str, client_secret: str, refresh_token: str) -> HueToken:
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        hue_token = self.get_hue_token(client_id=client_id, client_secret=client_secret, data=data)
        return hue_token

    def renew_hue_token(self, client_id: str, client_secret: str, hue_token: str) -> HueToken:
        if hue_token.is_expired:
            hue_token = self.refresh_hue_token(client_id=client_id, client_secret=client_secret, refresh_token=hue_token.refresh_token)
        return hue_token
    
    def get_hue_token(self, client_id: str, client_secret: str, data: Dict[str, str]) -> HueToken:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_url = f"https://api.meethue.com/v2/oauth2/token"
        auth = HTTPDigestAuth(username=client_id, password=client_secret)
        response = requests.post(url=token_url, auth=auth, headers=headers, data=data)
        response_json = response.json()
        expire_at = time.time() + response_json.get("expires_in")
        hue_token = HueToken(
            access_token=response_json.get("access_token"),
            expires_at=expire_at,
            refresh_token=response_json.get("refresh_token"),
            token_type="bearer"
        )
        keyring.set_password("hue-sdk", "refresh-token", hue_token.refresh_token)
        return hue_token

    def build(self, client_id: str, client_secret: str, code: str | None = None, hue_token: HueToken | None = None) -> HueToken:
        if code:
            hue_token = self.request_hue_token(client_id=client_id, client_secret=client_secret, code=code)
        elif hue_token:
            hue_token = self.renew_hue_token(client_id=client_id, client_secret=client_secret, hue_token=hue_token)
        else:
            refresh_token = keyring.get_password("hue-sdk", "refresh-token")
            if refresh_token:
                hue_token = self.refresh_hue_token(client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)
            else:
                print("error")
        return hue_token