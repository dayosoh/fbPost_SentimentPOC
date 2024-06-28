from openai import OpenAI
import os
from backend.models import add_post, get_latest_posts
from dotenv import load_dotenv

# Load environment variable using python-dotenv
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print("OpenAI API Key:", api_key)
if not api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables")

client = OpenAI(api_key=api_key)

def preprocess_text(text):
    # For now lets delete leading and trailing spaces, Add any preprocessing steps if needed
    return text.strip()

def classify_sentiment(text, user_prompt=None):
    examples = get_latest_posts()
    examples_text = "\n".join([f"Post: {ex['post_text']} -> Sentiment: {ex['sentiment']}" for ex in examples])
    
    if user_prompt:
        full_prompt = f"{user_prompt}\n{examples_text}\nClassify the sentiment of the following post:\nPost: {text}\nSentiment:"
    else:
        full_prompt = f"{examples_text}\nClassify the sentiment of the following post:\nPost: {text}\nSentiment:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a compliance officer that classifies the sentiment of posts."},
            {"role": "user", "content": full_prompt}
        ]
    )

    cGPTresponse = response.choices[0].message.content.strip()
    # Extract the sentiment from the ChatGPT response (you may need to adjust this based on the actual response format)
    if "Very Positive" in cGPTresponse:
        sentiment = "Very Positive"
    elif "Positive" in cGPTresponse:
        sentiment = "Positive"
    elif "Neutral" in cGPTresponse:
        sentiment = "Neutral"
    elif "Negative" in cGPTresponse:
        sentiment = "Negative"
    elif "Very Negative" in cGPTresponse:
        sentiment = "Very Negative"
    else:
        sentiment = "Unknown"  # Default in case the response doesn't match expected values

    return cGPTresponse, sentiment

def process_and_save_post(text, user_prompt=None):
    preprocessed_text = preprocess_text(text)
    cGPTresponse, sentiment = classify_sentiment(preprocessed_text, user_prompt)
    add_post(preprocessed_text, cGPTresponse, sentiment)
    return sentiment
