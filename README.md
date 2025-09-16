# Customer & Sales Management System

A simple Flask web application to manage customers and sales with a dashboard overview.
It includes CRUD operations, Bootstrap-based UI, and interactive charts for sales analysis.

## Features

- Dashboard
    - Yearly & monthly sales line chart
    - Top selling products pie chart
- Customers
    - Add, list, view details in modal
    - View related sales per customer
    - Delete customers
- Sales
    - Add and list sales
    - Delete sales
- Bootstrap UI
- SQLite databes (via SQLAlchemy ORM)
- Dockerized for easy deployment
---
## Tech stack

- Flask
- SQLAlchemy
- Bootstrap 5
- Chart.js
- Docker
---
## Installation (Local)
1. Clone the repository:
```
git clone https://github.com/yourusername/customer-sales-app.git
cd customer-sales-app
```
2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```
3. Initialize the database:
```
flask shell
>>> from models import db
>>> db.create_all()
>>> exit
```
4. Run the server:
```
flask run
```
---
## Running with Docker
1. Build and start the container:
```
docker-compose up --build
```
2. Access the app at:
```
http://localhost:5000
```
3. Stop the container:
```
docker-compose down
```
---