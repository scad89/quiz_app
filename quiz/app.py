import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from views import app_route

load_dotenv()


app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS"))
app.register_blueprint(app_route)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
