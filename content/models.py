from content import database
from datetime import datetime

class Users(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(200), nullable=False)
    email = database.Column(database.String(120), nullable=False, unique=True)
    date_added = database.Column(database.DateTime, default=datetime.utcnow)

    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name