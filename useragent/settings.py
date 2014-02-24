"""App configuration."""


from os import environ


##### DEBUG
DEBUG = True if environ.get('DEBUG') else False


##### DATABASE
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SQLALCHEMY_POOL_SIZE = 20
