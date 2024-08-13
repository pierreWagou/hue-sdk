from hue.sdk.metadata import Metadata
from hue.sdk.light.function import Function

class LightMetadata(Metadata):

    fixed_mired: int | None = None
    function: Function