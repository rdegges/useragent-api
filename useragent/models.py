"""Database models."""


from . import db


class UserAgent(db.Model):
    """A globally unique User Agent string."""

    __tablename__ = 'user_agents'
    string = db.Column(db.Text(), primary_key=True)

    def __repr__(self):
        """Return a human readable version of this model."""
        return u'<UserAgent: "%s">' % self.string
