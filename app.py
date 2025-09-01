from flask import Flask
from models import db
from routes.customer import bp_customer
from routes.sales import bp_sales

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(bp_customer)
    app.register_blueprint(bp_sales)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)