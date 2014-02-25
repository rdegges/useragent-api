"""Management commands."""


from BeautifulSoup import BeautifulSoup
from flask.ext.script import Manager
from requests import get
from sqlalchemy.exc import IntegrityError

from useragent import app, db
from useragent.models import UserAgent


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
def upload_user_agents():
    """Upload all User Agents into our PostgreSQL database."""
    for user_agent in fetch_user_agents():
        ua = UserAgent(string=user_agent)
        db.session.add(ua)

        try:
            db.session.commit()
            print 'Added User Agent:', ua.string
        except IntegrityError:
            db.session.rollback()


@manager.command
def ping():
    """Ping this Heroku application to keep it running."""
    get('http://api.useragent.io')


##### HELPERS
def fetch_user_agents():
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

    return list(set(user_agents))


if __name__ == '__main__':
    manager.run()
