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

# CRUD for Customers
@app.post("/customers")
def create_customer(customer: Customer):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (customer.name, customer.email))
        conn.commit()
        return {"message": "Customer created successfully!"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Customer email already exists.")
    finally:
        conn.close()

@app.get("/customers/{id}")
def get_customer(id: int):
    conn = get_db_connection()
    customer = conn.execute("SELECT * FROM customers WHERE id = ?", (id,)).fetchone()
    conn.close()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found.")
    return dict(customer)

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customer):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET name = ?, email = ? WHERE id = ?", (customer.name, customer.email, id))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found.")
    return {"message": "Customer updated successfully."}

@app.delete("/customers/{id}")
def delete_customer(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found.")
    return {"message": "Customer deleted successfully."}

# CRUD for Items
@app.post("/items")
def create_item(item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
    conn.commit()
    conn.close()
    return {"message": "Item created successfully!"}
 
@app.get("/items/{id}")
def get_item(id: int):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
    conn.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    return dict(item)
 
@app.put("/items/{id}")
def update_item(id: int, item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name = ?, price = ? WHERE id = ?", (item.name, item.price, id))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"message": "Item updated successfully."}
 
@app.delete("/items/{id}")
def delete_item(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"message": "Item deleted successfully."}