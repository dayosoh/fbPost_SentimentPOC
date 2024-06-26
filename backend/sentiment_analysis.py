import openai
import os
from .models import add_post, get_latest_posts

openai.api_key = os.getenv('OPENAI_API_KEY')

def preprocess_text(text):
    # Add any preprocessing steps if needed
    return text.strip()

def classify_sentiment(text):
    examples = get_latest_posts()
    examples_text = "\n".join([f"Post: {ex['post_text']} -> Sentiment: {ex['sentiment']}" for ex in examples])
    prompt = f"Classify the sentiment of the following post:\n{examples_text}\nPost: {text}\nSentiment:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10
    )
    
    sentiment = response.choices[0].text.strip()
    return sentiment

def process_and_save_post(text):
    preprocessed_text = preprocess_text(text)
    sentiment = classify_sentiment(preprocessed_text)
    add_post(preprocessed_text, sentiment)
    return sentiment
