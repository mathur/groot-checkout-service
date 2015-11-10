import datetime

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime)
    name = db.Column(db.String(140), unique=True)
    description = db.Column(db.String(320))
    in_inventory = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer)

    def __init__(self, name, description, in_inventory, user_id):
        self.name = name
        self.description = description
        self.in_inventory = in_inventory
        self.user_id = user_id
        self.time_created = datetime.datetime.now()

    def __repr__(self):
        return '<Item %r>' % self.id

class Book(Item):
    __tablename__ = 'books'

    author = db.Column(db.String(140))

    def __init__(self, name, author, description, in_inventory, user_id):
        Item.__init__(self, name, description, in_inventory, user_id)
        self.author = author

    def __repr__(self):
        return '<Book %r>' % self.id

class Hardware(Item):
    __tablename__ = 'hardware'

    manufacturer = db.Column(db.String(140))

    def __init__(self, name, manufacturer, description, in_inventory, user_id):
        Item.__init__(self, name, description, in_inventory, user_id)
        self.manufacturer = manufacturer

    def __repr__(self):
        return '<Book %r>' % self.id