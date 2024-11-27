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