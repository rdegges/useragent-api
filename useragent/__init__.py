"""App setup and initialization."""


from flask import Flask


##### GLOBALS
app = Flask(__name__)
app.config.from_pyfile('settings.py')
