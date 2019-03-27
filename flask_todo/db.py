import psycopg2

def get_db():
    connection = psycopg2.connect(host = "127.0.0.0", database = "todo")
    cursor = connection.cursor()

def close_db():
    cursor.close()
    connection.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
