from flask import Flask, request, jsonify
from .database import init_db
from .models import get_latest_posts, update_sentiment
from .sentiment_analysis import process_and_save_post

app = Flask(__name__)

init_db()

@app.route('/ingest', methods=['POST'])
def ingest():
    post_text = request.json['post_text']
    sentiment = process_and_save_post(post_text)
    return jsonify({"sentiment": sentiment})

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = get_latest_posts()
    return jsonify([dict(post) for post in posts])

@app.route('/update_sentiment', methods=['POST'])
def update():
    post_id = request.json['post_id']
    sentiment = request.json['sentiment']
    update_sentiment(post_id, sentiment)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
