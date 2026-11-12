from pydantic import BaseModel


# Model for representing a product
class Product(BaseModel):
    id: int
    name: str
    price: float
