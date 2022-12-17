from pydantic import BaseModel

class Prod(BaseModel):
    _id: str
    prod_name: str
    prod_price: int
    channel: str
    created_at: str
