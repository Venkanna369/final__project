# app/database.py or main.py
import sqlite3

def get_db_connection(test_mode=False):
    if test_mode:
        conn = sqlite3.connect(":memory:") 
    else:
        conn = sqlite3.connect("db.sqlite")
    conn.row_factory = sqlite3.Row
    return conn
