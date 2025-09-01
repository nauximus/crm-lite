from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Sale, Customer
from sqlalchemy import extract, func
from collections import Counter
from datetime import datetime

bp_sales = Blueprint("sales", __name__, url_prefix="/sales")

# Sales list
@bp_sales.route("/")
def list_sales():
    all_sales = Sale.query.all()

    return render_template("sales.html", sales=all_sales)

@bp_sales.route("/add", methods=["GET", "POST"])
def add_sale():
    customers = Customer.query.all()
    if request.method == "POST":
        product = request.form["product"]
        amount = int(request.form["amount"])
        price = float(request.form["price"])
        customer_id = int(request.form["customer_id"])
        date_str = request.form.get("date")
        date = datetime.strftime(date_str, "%d-%m-%Y") if date_str else datetime.now()

        new_sale = Sale(
            product=product, 
            amount=amount, 
            price=price, 
            customer_id=customer_id,
            date=date
        )
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for("sales.list_sales"))
    return render_template("add_sale.html", customers=customers)

@bp_sales.route("/delete/<int:sale_id>")
def delete_sale(sale_id):
    sale = Sale.query.get_or_404(sale_id)
    db.session.delete(sale)
    db.session.commit()
    return redirect(url_for("sales.list_sales"))