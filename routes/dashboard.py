from flask import Blueprint, render_template
from models import db, Sale
from sqlalchemy import func
from datetime import datetime

bp_dashboard = Blueprint("dashboard", __name__)

@bp_dashboard.route("/")
def index():
    # Yearly and monthly sales
    current_year = datetime.now().year
    monthly_sales = (
        db.session.query(
            func.strftime("%Y-%m", Sale.date).label("month"),
            func.sum(Sale.amount * Sale.price).label("total")
        )
        .filter(func.strftime("%Y", Sale.date) == str(current_year))
        .group_by("month")
        .all()
    )
    top_products = (
        db.session.query(
            Sale.product,
            func.sum(Sale.amount).label("total_sold")
        )
        .group_by(Sale.product)
        .order_by(func.sum(Sale.amount).desc())
    )

    # Chart.js conversion to JSON
    monthly_labels = [row[0] for row in monthly_sales]
    monthly_totals = [row[1] for row in monthly_sales]

    product_labels = [row[0] for row in top_products]
    product_totals = [row[1] for row in top_products]

    return render_template(
        "index.html",
        monthly_labels=monthly_labels,
        monthly_totals=monthly_totals,
        product_labels=product_labels,
        product_totals=product_totals
    )