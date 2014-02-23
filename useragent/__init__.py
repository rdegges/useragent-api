"""App setup and initialization."""


from flask import Flask


##### GLOBALS
app = Flask(__name__)
app.config.from_pyfile('settings.py')


##### API
from .api import get_random_user_agent
