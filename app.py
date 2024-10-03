# app.py

from flask import Flask
from config.mongo_config import get_mongo_client

app = Flask(__name__)

# Initialize MongoDB client
mongo_client = get_mongo_client()

@app.route("/")
def home():
    return "<p>Hello, World!</p>"
