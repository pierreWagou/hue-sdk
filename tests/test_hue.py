from hue.sdk.client.client import HueClient, LightClient
from hue.sdk.client.token import HueToken,  HueTokenFactory
from hue.sdk.light.light import Light
from hue.sdk.light.light_put import LightPut

client_id="cP0EeCvVucL3271s9xHR4yDvXDGACMHE"
client_secret="OmOzQo6waQitb0Wd"

def test_token():
    token_url = "https://api.meethue.com/v2/oauth"
    token = HueTokenFactory(token_url=token_url).build(client_id=client_id, client_secret=client_secret)
    assert isinstance(token, HueToken)

def test_get_light():
    client = HueClient(
        client_id=client_id,
        client_secret=client_secret,
    )
    light = client.light.get(light_id="3c20738a-b6ee-4752-9d19-593adcad6509")
    assert isinstance(light, Light)

def test_update_light():
    light_id = "3c20738a-b6ee-4752-9d19-593adcad6509"
    client = HueClient(
        client_id=client_id,
        client_secret=client_secret,
    )
    light = client.light.get(light_id=light_id)
    light.on.on = False
    light = LightPut(on=light.on)
    client.light.update(light_id=light_id, light=light)
    updated_light = client.light.get(light_id=light_id)
    assert updated_light.on.on == False