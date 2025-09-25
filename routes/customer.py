from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from models import db, Customer, Sale

bp_customer = Blueprint("customer", __name__, url_prefix="/customers")

# Customer list
@bp_customer.route("/")
def list_customers():
    all_customers = Customer.query.all()
    return render_template("customers.html", customers=all_customers)

# Add new customer
@bp_customer.route("/add", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form.get("phone")
        company = request.form.get("company")
        notes = request.form.get("notes")

        new_customer = Customer(
            name=name, email=email, phone=phone, company=company, notes=notes
        )
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for("customer.list_customers"))
    
    return render_template("add_customer.html")

@bp_customer.route("/<int:customer_id>")
def customer_detail(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    sales = Sale.query.filter_by(customer_id=customer.id).all()
    return render_template("customer_detail.html", customer=customer, sales=sales)

@bp_customer.route("/<int:customer_id>/json")
def customer_json(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    sales = Sale.query.filter_by(customer_id=customer.id).all()
    sales_list = [
        {
            "product": s.product,
            "amount": s.amount,
            "price": s.price,
            "date": s.date.to_char("%Y-%m-%d")
        } for s in sales
    ]
    return jsonify({
        "name": customer.name,
        "email": customer.email,
        "phone": customer.phone,
        "company": customer.company,
        "notes": customer.notes,
        "sales": sales_list
    })

# Delete customer
@bp_customer.route('/<int:customer_id>/delete', methods=['POST'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    for sale in customer.sales:
        db.session.delete(sale)
    
    db.session.delete(customer)
    db.session.commit()
    flash("Customer deleted successfully.", "success")
    return redirect(url_for("customer.list_customers"))