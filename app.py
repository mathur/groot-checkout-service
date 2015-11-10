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
    elif type_of_item == 'hardware'
        hardware_items = Hardware.query.all()
        for hardware in hardware_items:
            print hardware
    else:
        items = Item.query.all()
        for item in items:
            print item

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    db.init_app(app)
    app.run(host='0.0.0.0', port=port, debug=True)