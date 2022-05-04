import os
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask import Flask, render_template, session, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from .models import QuizQuestion
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS"))
db = SQLAlchemy(app)
db.create_all()
