from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import get_db_connection
import sqlite3

app = FastAPI()

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