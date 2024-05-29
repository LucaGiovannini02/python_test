import sqlite3 as sq

def get_db():
    conn = sq.connect('../CodiceFiscale.sqlite3')
    conn.row_factory = sq.Row
    return conn
