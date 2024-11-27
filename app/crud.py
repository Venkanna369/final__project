from app.database import get_db_connection

# CRUD for Customers
def create_customer(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def get_customer(id):
    conn = get_db_connection()
    customer = conn.execute("SELECT * FROM customers WHERE id = ?", (id,)).fetchone()
    conn.close()
    return customer

def update_customer(id, name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_customer(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

# CRUD for Items
def create_item(name, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()
 
def get_item(id):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
    conn.close()
    return item
 
def update_item(id, name, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name = ?, price = ? WHERE id = ?", (name, price, id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated
 
def delete_item(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

# CRUD for Orders
def create_order(customer_id, item_id, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    customer = conn.execute("SELECT id FROM customers WHERE id = ?", (customer_id,)).fetchone()
    item = conn.execute("SELECT id FROM items WHERE id = ?", (item_id,)).fetchone()
    if not customer or not item:
        conn.close()
        raise ValueError("Invalid customer_id or item_id.")
    cursor.execute("INSERT INTO orders (customer_id, item_id, quantity) VALUES (?, ?, ?)",
                   (customer_id, item_id, quantity))
    conn.commit()
    conn.close()
 
def get_order(id):
    conn = get_db_connection()
    order = conn.execute("SELECT * FROM orders WHERE id = ?", (id,)).fetchone()
    conn.close()
    return order
 
def update_order(id, customer_id, item_id, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET customer_id = ?, item_id = ?, quantity = ? WHERE id = ?",
                   (customer_id, item_id, quantity, id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated
 
def delete_order(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE id = ?", (id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted