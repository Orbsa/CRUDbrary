from db import *

def create_table(): # It may be more appropriate to use a schema sql file..
    ''' Create the database table if it's not already there
    should have title, author, isbn
    rented to be ISO8601 corresponding to time of last rental
    availble is boolean integer '''

    table = """CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT NOT NULL,
                rented TEXT,
                available INT
            )
            """
    db = get_db()
    c = db.cursor()
    c.execute(table)
    c.close()
    return True

def clear_table():
    db = get_db()
    query_db('DROP TABLE books') # Out with the old
    create_table() # In with the new

def get(book):
    statement = "SELECT * FROM books WHERE id = ?"
    return query_db(statement, [book['id']], one=True)

def get_all():
    statement = "SELECT id, title, author, isbn FROM books"
    return query_db(statement)

def insert(book):
    statement = "INSERT INTO books(title, author, isbn) VALUES (?,?,?)"
    return query_db(statement, [book['title'], book['author'], book['isbn']], one = True)

def update(updated_keys):
    book = get(updated_keys)
    for key in updated_keys: book[key] = updated_keys[key]
    statement = "UPDATE books SET title=?, author=?, isbn=? WHERE id = ?"
    return query_db(statement, [book['title'], book['author'], book['isbn'], book['id']], one = True)

def delete(book):
    statement = "DELETE FROM books WHERE id = ?"
    return query_db(statement, [book['id']], one = True)
