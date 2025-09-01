from flask import Blueprint, render_template
from models import Customer, Sale, db
from collections import Counter
from datetime import datetime

bp_dashboard = Blueprint("dashboard", __name__)

@bp_dashboard.route("/")
def index():
    # Customer data
    customers = Customer.query.order_by(Customer.id.desc()).all()
    total_customers = len(customers)

    # Sales data
    sales = Sale.query.order_by(Sale.date.desc()).all()
    total_sales = sum([s.price * s.amount for s in sales])
    
    # --- Line chart data ---
    monthly_salets_data = [0]*12
    current_year = datetime.now().year
    for s in sales:
        if s.date.year == current_year:
            monthly_salets_data[s.date.month-1] += s.price * s.amount
    monthly_labels = [ "January, February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November"]
    
    # --- Pie chart data ---
    product_counter = Counter()
    for s in sales:
        product_counter[s.product] += s.amount

    top_products = product_counter.most_common(5)