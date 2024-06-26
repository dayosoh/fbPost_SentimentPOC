import sqlite3

def init_db():
    conn = sqlite3.connect('fbpost_sentiment.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            post_text TEXT NOT NULL,
            sentiment TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('fbpost_sentiment.db')
    conn.row_factory = sqlite3.Row
    return conn
