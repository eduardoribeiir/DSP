from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    due_date: str