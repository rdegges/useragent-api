"""Management commands."""


from flask.ext.script import Manager

from useragent import app


##### GLOBALS
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
