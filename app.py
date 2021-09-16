import json
import requests
from flask import Flask, request, jsonify, make_response, g, abort

import books_controller as BC
import db

# Initialize Flask app
app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db.close()

@app.route('/')
def index():
    return make_response('Go to /init to initialize the database!',200)

@app.route('/api/v1/books', methods=['GET'])
def fetch_all_books():
    books = BC.get_all()
    return jsonify(books)

@app.route('/api/v1/book', methods=['GET'])
def fetch_book():
    args = request.get_json()
    if not args or 'id' not in args:
        return make_response("id is a required json body parameter for this request",400)
    book = BC.get(args)
    if not book: abort(404)
    return jsonify(book)

@app.route('/api/v1/book', methods=['POST'])
def insert_book():
    args = request.get_json()
    reqParams = ['title', 'author', 'isbn']
    if not args or not all([param in args for param in reqParams]):
        return make_response("[title, author, isbn] are required json body parameters for this request",400)
    book = BC.insert(args) # Unpack reqParams from load to send to controller
    return jsonify(book)

@app.route('/api/v1/book', methods=['PUT'])
def update_book():
    args = request.get_json()
    if not args or 'id' not in args:
        return make_response("id is a required json body parameter for this request",400)
    reqParams = ['title', 'author', 'isbn']
    if not any([param in args for param in reqParams]):
        return make_response("any of [title, author, isbn] required json body parameters for this request",400)
    book = BC.update(args)
    print(book)
    if not book: abort(404)
    return jsonify(BC.get(args))

@app.route('/api/v1/book', methods=['DELETE'])
def delete_book():
    args = request.get_json()
    if not args or 'id' not in args:
        return make_response("id is a required json body parameter for this request",400)
    book = BC.delete(args)
    return jsonify(book)

def load_books():
    '''Inserts Penguin's latest 10 books'''
    load = request.get_json()
    payload = {
            'q': 'inpublisher penguin',
            'orderBy' : 'newest',
            'maxResults' : 10
            }
    r = requests.get('https://www.googleapis.com/books/v1/volumes', params = payload)
    js = r.json()
    for book in js['items']:
        book = book['volumeInfo']
        new_book = {
            'title':book['title'],
            'author':book['author'] if 'author' in book else book['authors'][0],
            'isbn':book['industryIdentifiers'][0]['identifier']
            }
        BC.insert(new_book)

@app.route('/init')
def init_db():
    BC.create_table()
    load_books()
    return make_response('Success!', 200)
