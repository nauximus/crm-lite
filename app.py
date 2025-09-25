import os
import time
from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import create_engine
from models import db
from routes.dashboard import bp_dashboard
from routes.customer import bp_customer
from routes.sales import bp_sales

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        conn = engine.connect()
        conn.close()
        print("DB connected")
        break
    except Exception as e:
        print(f"DB not ready, retrying... {i+1}/10")
        time.sleep(3)
else:
    raise Exception("Cannot connect to DB")

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "devsecret")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(bp_dashboard)
    app.register_blueprint(bp_customer)
    app.register_blueprint(bp_sales)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)