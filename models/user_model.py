# models/user_model.py

from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.testflask
users_collection = db.flaskusers

class User:
    @staticmethod
    def create_user(full_name, email, password):
        password_hash = generate_password_hash(password)
        user = {
            "full_name": full_name,
            "email": email,
            "password": password_hash
        }
        users_collection.insert_one(user)
        return user

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one({"email": email})

    @staticmethod
    def check_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)
