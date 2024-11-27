from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    email: str

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    customer_id: int
    item_id: int
    quantity: int
