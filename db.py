from flask import g
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# Initialize flask sqlite connection
database_filename = 'library.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g_database = sqlite3.connect(database_filename)
    return db


def create_table():
    ''' Create the database table if it's not already there
    should have title, author, isbn
    rented to be ISO8601 corresponding to time of last rental
    availble is boolean integer '''

    book = """CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL,
                rented TEXT,
                available INT,
            )
            """
    db = get_db()
    db.cursor().execute(table)
    return True

def get_books(id):
    db = get_db()
    c = db.cursor()
    statement = "SELECT id, title, author, isbn FROM books"
    c.execute(statement, [id])
    return c.fetchall()

def insert_book(title, author, isbn):
    db = get_db()
    c = db.cursor()
    statement = "INSERT INTO books(title, author, isbn) VALUES (?,?,?)"
    c.execute(statement, [title, author, isbn])
    db.commit()
    return True

def update_book(id, title, author, isbn):
    db = get_db()
    c = db.cursor()
    statement = "UPDATE books SET title=?, author=?, isbn=? WHERE id = ?"
    c.execute(statement, [title, author, isbn, id])
    db.commit()
    return True

def delete_book(id):
    db = get_db()
    c = db.cursor()
    statement = "DELETE FROM books WHERE id = ?"
    c.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    c = db.cursor()
    statement = "SELECT FROM books WHERE id = ?"
    c.execute(statement, [id])
    return c.fetchone()


