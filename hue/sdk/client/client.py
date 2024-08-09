from hue.sdk.client.token import HueToken
from hue.sdk.client.session import HueSession

class HueClient:

    def __init__(self, client_id: str, client_secret: str, code: str | None = None, hue_token: HueToken | None = None):
        self.hue_session = HueSession(client_id=client_id, client_secret=client_secret, code=code, hue_token=hue_token)

    def list_light(self):
        light_list = self.hue_session.get(url="light")
        light_list = light_list.json()
        return light_list
    
    def get_light(self, light_id: str):
        endpoint = f"light/{light_id}"
        light_data = self.hue_session.get(url=endpoint)[0]
        print(light_data)
        return light_data
