# models/user_model.py

from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.testflask
users_collection = db.flaskusers

# Create a unique index on the email field
users_collection.create_index("email", unique=True)

class User:
    @staticmethod
    def create_user(full_name, email, password):
        password_hash = generate_password_hash(password)
        user = {
            "full_name": full_name,
            "email": email,
            "password": password_hash
        }
        try:
            users_collection.insert_one(user)
            return user
        except Exception as e:
            # Return an error if the email is already in use
            return {"error": str(e)}

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one({"email": email})
