import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv
from views import QuestionView

load_dotenv()


app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS"))
api = Api(app)
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
api.add_resource(QuestionView, '/question')


if __name__ == '__main__':
    app.run()
