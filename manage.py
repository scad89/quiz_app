#!/usr/bin/env python
import os
from flask_script import Manager
from quiz import create_app
from dotenv import load_dotenv

load_dotenv()


app = create_app()
app.config.from_object(os.environ.get("APP_SETTINGS"))
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
