"""App setup and initialization."""


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


##### GLOBALS
app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)


##### MODELS
from .models import *


##### API
from .api import *
