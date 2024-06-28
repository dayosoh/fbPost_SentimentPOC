from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.database import init_db
from backend.models import get_latest_posts, update_sentiment
from backend.sentiment_analysis import process_and_save_post
import logging
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

init_db()
logging.basicConfig(level=logging.DEBUG)

@app.route('/ingest', methods=['POST'])
def ingest():
    logging.debug("Received ingest request")
    data = request.json
    logging.debug(f"Request data: {data}")
    
    if not data or 'post_text' not in data:
        logging.error("Invalid request data")
        return jsonify({"error": "Invalid request data"}), 400
    
    post_text = data.get('post_text')
    user_prompt = data.get('user_prompt')
    logging.debug(f"Post text: {post_text}, User prompt: {user_prompt}")

    try:
        sentiment = process_and_save_post(post_text, user_prompt)
        logging.debug(f"Processed sentiment: {sentiment}")
        return jsonify({"sentiment": sentiment})
    except Exception as e:
        logging.error(f"Error processing post: {e}")
        return jsonify({"error": "Failed to process post"}), 500
    
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
