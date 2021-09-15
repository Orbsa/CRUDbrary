import json
import requests
from flask import Flask, request, jsonify, make_response, g

from db import *

# Initialize Flask app
app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    get_db().close()

@app.route('/')
def index():
    return make_response('Jello World!',200)

@app.route('/test')
def test_repeater():
    payload = {
            'q':"Harry Potter",
            'maxResults': "7"
            }
    r = requests.get('https://www.googleapis.com/books/v1/volumes', params = payload)
    js = r.json()
    titles = []
    for book in js['items']:
        titles.append(book["volumeInfo"]["title"])
    return make_response(jsonify(titles), 200)

@app.route('/api/v1/books', methods=['GET'])
def get_books():
    pass


class Book():
    pass