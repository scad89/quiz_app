import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = os.environ.get("DEBUG")
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=os.environ.get('POSTGRES_USER'),
                                                                                    pw=os.environ.get(
                                                                                        'POSTGRES_PASSWORD'),
                                                                                    url=os.environ.get(
                                                                                        'POSTGRES_HOST'),
                                                                                    db=os.environ.get('POSTGRES_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
