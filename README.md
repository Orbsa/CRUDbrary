# CRUDbrary

This is used to demonstrate a CRUD API built ontop of flask and SQLite

#### Dependencies
* flask
* requests


#### To Use
1. Install dependencies through pip(venv)
1. Clone project
1. Change into the project's root directory
1. 'flask run'
1. make a GET request to `http://127.0.0.1:5000/init` to initialize the database
  1. Any future requests here, will clean the table fresh again
1. Requests can now be made to the `http://127.0.0.1:5000/api/v1/` endpoint
  1. `api/v1/books` - A GET request will return an array of all book objects stored in the DB
  1. `api/v1/book` - ALL arguments must be passed in through JSON in the body of the request
    1. A GET request with an `ID` will return the corresponding book, if any, and a 404 if none is found
    1. A POST request with `author` `title` & `isbn` keys in the JSON Body will create a new book in the DB
    1. A PUT request requires `ID` and any of the above keys will be updated on the associated book if any is found
    1. A DELETE request requires 'ID'. It will delete any books found with that unique ID in the database
