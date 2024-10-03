# config/mongo_config.py

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the MongoDB URI from the environment variable
MONGODB_URI = os.getenv('MONGODB_URI')

def get_mongo_client():
    try:
        client = MongoClient(MONGODB_URI)
        # Print success message if connected successfully
        print("MongoDB connected successfully!")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
