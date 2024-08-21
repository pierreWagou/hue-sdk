from pydantic import BaseModel

class Identify(BaseModel):

    action: str = "identify"