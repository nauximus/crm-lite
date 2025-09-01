from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    notes = db.Column(db.Text)

    sales = db.relationship("Sale", backref="customer", lazy=True)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)