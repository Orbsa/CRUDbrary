from flask import g
import sqlite3

DB_FILENAME= 'library.db'

# Row Factory
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

# Initialize flask sqlite connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g_database = sqlite3.connect(DB_FILENAME)
    db.row_factory = make_dicts
    return db

# Make queries AND return results
def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    rv = cur.fetchall()
    db.commit()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Close the DB
def close():
    get_db().close()
