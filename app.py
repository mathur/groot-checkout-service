import os
from flask import Flask, jsonify, request
from models import db, Item, Book, Hardware
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

@app.route('/api/all', methods=['GET'])
def return_all():
    type_of_item = request.args['type']

    if type_of_item == 'book':
        book_items = Book.query.all()
        for book in book_items:
            print book
    elif type_of_item == 'hardware':
        hardware_items = Hardware.query.all()
        for hardware in hardware_items:
            print hardware
    else:
        items = Item.query.all()
        for item in items:
            print item

@app.route('/api/new', methods=['POST'])
def create_new():
    type_of_item = request.form['type']

    if type_of_item == 'book':
        name = request.form['name']
        author = request.form['author']
        description = request.form['description']
        in_inventory = True
        user_id = None
        book = Book(name, author, description, in_inventory, user_id)
        db.session.add(book)
        db.session.commit()
    elif type_of_item == 'hardware':
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        description = request.form['description']
        in_inventory = True
        user_id = None
        hardware = Book(name, manufacturer, description, in_inventory, user_id)
        db.session.add(hardware)
        db.session.commit()
    else:
        # return error json
        return

@app.route('/api/checkout', methods=['POST'])
def checkout():
    type_of_item = request.form['type']
    item_id = int(request.form['id'])
    user_id = int(request.form['user_id'])

    if type_of_item == 'book':
        book = Book.query.filter_by(id=item_id).first()
        book.user_id = user_id
        book.in_inventory = False
    elif type_of_item == 'hardware':
        hardware = Hardware.query.filter_by(id=item_id).first()
        hardware.user_id = user_id
        hardware.in_inventory = False
    else:
        # return error json
        return

@app.route('/api/checkin', methods=['POST'])
def checkout():
    type_of_item = request.form['type']
    item_id = int(request.form['id'])
    user_id = int(request.form['user_id'])

    if type_of_item == 'book':
        book = Book.query.filter_by(id=item_id).first()
        book.user_id = None
        book.in_inventory = True
    elif type_of_item == 'hardware':
        hardware = Hardware.query.filter_by(id=item_id).first()
        hardware.user_id = None
        hardware.in_inventory = True
    else:
        # return error json
        return

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    db.init_app(app)
    app.run(host='0.0.0.0', port=port, debug=True)