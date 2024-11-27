
# Final Project: REST API for Dosa Restaurant

## Overview
This project implements a REST API backend for a dosa restaurant using **FastAPI** and **SQLite**. The API provides CRUD functionality for the following entities:
- Customers
- Items (Dosa menu)
- Orders


---

## Features
1. **SQLite Database**
   - Persistent storage using `db.sqlite`.
   - Relational constraints between tables:
     - `customers` table: Stores customer information (name, email).
     - `items` table: Stores menu items (name, price).
     - `orders` table: Tracks orders with foreign key references to `customers` and `items`.

2. **FastAPI Framework**
   - Provides a lightweight, fast, and scalable REST API.
   - Implements endpoints for CRUD operations for all entities.

3. **Endpoints**
   - Customers:
     - `POST /customers`: Creates a new customer.
     - `GET /customers/{id}`: Retrieves a customer by ID.
     - `PUT /customers/{id}`: Updates an existing customer.
     - `DELETE /customers/{id}`: Deletes a customer by ID.
   - Items:
     - `POST /items`: Creates a new item.
     - `GET /items/{id}`: Retrieves an item by ID.
     - `PUT /items/{id}`: Updates an existing item.
     - `DELETE /items/{id}`: Deletes an item by ID.
   - Orders:
     - `POST /orders`: Creates a new order.
     - `GET /orders/{id}`: Retrieves an order by ID.
     - `PUT /orders/{id}`: Updates an existing order.
     - `DELETE /orders/{id}`: Deletes an order by ID.

4. **Database Initialization**
   - A script `init_db.py` initializes the database by creating the necessary tables.

---

## Setup Instructions

### Prerequisites
- Python 3.10 or later
- SQLite

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd final_project
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/macOS
   .venv\Scripts\activate   # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python app/init_db.py
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Sample Usage

### Create a Customer
```bash
curl -X POST "http://127.0.0.1:8000/customers" -H "Content-Type: application/json" -d '{"name": "Venkanna Dharavath", "email": "venkanna369@gmail.com"}'
```

### Get a Customer
```bash
curl -X GET "http://127.0.0.1:8000/customers/1"
```

### Create an Order
```bash
curl -X POST "http://127.0.0.1:8000/orders" -H "Content-Type: application/json" -d '{"customer_id": 1, "item_id": 2, "quantity": 3}'
```

---

## Database Schema

### Customers Table
| Column | Type   | Constraints        |
|--------|--------|--------------------|
| id     | INT    | PRIMARY KEY        |
| name   | TEXT   | NOT NULL           |
| email  | TEXT   | NOT NULL, UNIQUE   |

### Items Table
| Column | Type   | Constraints        |
|--------|--------|--------------------|
| id     | INT    | PRIMARY KEY        |
| name   | TEXT   | NOT NULL           |
| price  | REAL   | NOT NULL           |

### Orders Table
| Column      | Type   | Constraints                     |
|-------------|--------|---------------------------------|
| id          | INT    | PRIMARY KEY                     |
| customer_id | INT    | FOREIGN KEY (`customers.id`)    |
| item_id     | INT    | FOREIGN KEY (`items.id`)        |
| quantity    | INT    | NOT NULL                        |

---

## Requirements
- FastAPI
- SQLite
- Uvicorn (ASGI server)

Install using:
```bash
pip install fastapi uvicorn
```

---

## Notes
- Foreign key constraints are enabled in SQLite to ensure data integrity.
- Followed Python conventions and document changes in the commit messages.

---
