import psycopg2
from flask import current_app

def get_db():
    connection = psycopg2.connect(database = "todo")
    return connection

def close_db():
    if connection is not None:
        connection.close()

def init_db():
    db = get_db()
    cur = db.cursor()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def insert(item):
    db = get_db()
    cur = db.cursor()
    cur.execute( f"INSERT INTO objectives (todo) VALUES ({item});")

def retrieve(item):
    db = get_db()
    cursor = db.cursor()
    cur.execute(f"SELECT {item} FROM todo;")
    return item
