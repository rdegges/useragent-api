"""Management commands."""


from BeautifulSoup import BeautifulSoup
from flask.ext.script import Manager
from requests import get

from useragent import app, db


##### GLOBALS
manager = Manager(app)
allowed_agents = [
    'america online browser',
    'aolbuild',
    'chrome',
    'chromium',
    'chromeplus',
    'epiphany',
    'firefox',
    'iceweasel',
    'konqueror',
    'mozilla',
    'namoroka',
    'opera',
    'safari',
    'seamonkey',
]


##### SCRIPTS
@manager.command
def initdb():
    """Initialize the PostgreSQL database."""
    db.create_all()


@manager.command
def rmdb():
    """Destroy the PostgreSQL database."""
    db.drop_all()


@manager.command
def fetch_uas():
    """
    Scrape this page: http://www.useragentstring.com/pages/All/ (which returns
    every User Agent string known to man), then strip the list down to only the
    modern browser user agents.
    """
    resp = get('http://www.useragentstring.com/pages/All/')
    if resp.status_code != 200:
        print 'Failed to fetch: http://www.useragentstring.com/pages/All/'
        return

    soup = BeautifulSoup(resp.text)
    user_agents = []
    for user_agent in [elem.first().getText() for elem in soup.findAll('li')]:
        for agent in allowed_agents:
            if agent in user_agent.lower():
                user_agents.append(user_agent)

    for user_agent in user_agents:
        print user_agent


if __name__ == '__main__':
    manager.run()
