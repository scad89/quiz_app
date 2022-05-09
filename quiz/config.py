import os
from dotenv import load_dotenv

load_dotenv()


DEBUG = os.environ.get("DEBUG")
CSRF_ENABLED = os.environ.get("CSRF_ENABLED")
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}:{port}/{db}'.format(user=os.environ.get('POSTGRES_USER'),
                                                                                       pw=os.environ.get(
                                                                                           'POSTGRES_PASSWORD'),
                                                                                       url=os.environ.get(
                                                                                           'POSTGRES_HOST'),
                                                                                       port=os.environ.get(
                                                                                           'POSTGRES_PORT'),
                                                                                       db=os.environ.get('POSTGRES_NAME'))
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS")
