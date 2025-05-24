from pydantic import BaseModel

class CoffeeModel(BaseModel):
    name: str
    origin: str
    roast_level: str 