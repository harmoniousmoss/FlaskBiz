# models/contact_model.py

from pymongo import MongoClient
import os
from bson import ObjectId  # Import ObjectId
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.testflask
contacts_collection = db.flaskcontacts

class Contact:
    @staticmethod
    def create_contact(full_name, email, phone_number, message):
        contact = {
            "full_name": full_name,
            "email": email,
            "phone_number": phone_number,
            "message": message
        }
        result = contacts_collection.insert_one(contact)
        contact["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return contact
