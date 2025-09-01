from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Customer

bp_customer = Blueprint("customer", __name__, url_prefix="/customers")

# Customer list
@bp_customer.route("/")
def list_customers():
    all_customers = Customer.query.all()
    return render_template("customers.html", customers=all_customers)

# Add new customer
@bp_customer.route("/customers/add", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form("phone")
        company = request.form("company")
        notes = request.form("notes")

        new_customer = Customer(
            name=name, email=email, phone=phone, company=company, notes=notes
        )
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for("customer.list_customers"))
    
    return render_template("add_customer.html")

# Delete customer
@bp_customer.route("/delete/<int:customer_id>")
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("customer.list_customers"))