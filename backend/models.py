from backend.database import get_db_connection

def add_post(post_text, cGPTresponse, sentiment):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO posts (post_text, cGPTresponse, sentiment) VALUES (?, ?, ?)', (post_text, cGPTresponse, sentiment))
    conn.commit()
    conn.close()

def get_latest_posts(limit=10):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM posts ORDER BY timestamp DESC LIMIT ?', (limit,))
    posts = c.fetchall()
    conn.close()
    return posts

def update_sentiment(post_id, sentiment):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('UPDATE posts SET sentiment = ? WHERE id = ?', (sentiment, post_id))
    conn.commit()
    conn.close()
