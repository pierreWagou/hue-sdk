from hue.sdk.client.client import HueClient
from hue.sdk.data.product_data import ProductData
from hue.sdk.data.function import Function
from hue.sdk.client.token import HueToken,  HueTokenFactory
from hue.sdk.light.light import Light


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
    light = client.get_light(light_id="3c20738a-b6ee-4752-9d19-593adcad6509")
    assert isinstance(light, Light)

def test_hue():
    ProductData(name="test", function=Function.DECORATIVE)