import os
from flask import Flask
from .database import db
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get("APP_SETTINGS"))

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    return app
