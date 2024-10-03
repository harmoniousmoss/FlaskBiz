# models/news_model.py

from pymongo import MongoClient
from datetime import datetime, timezone
import os
from dotenv import load_dotenv
import boto3

load_dotenv()

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client.testflask
news_collection = db.flasknews

# AWS S3 setup
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)
bucket_name = os.getenv("AWS_BUCKET_NAME")

class News:
    @staticmethod
    def upload_news_cover(file):
        file_name = file.filename
        try:
            s3.upload_fileobj(file, bucket_name, file_name)
            file_url = f"https://{bucket_name}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{file_name}"
            return file_url
        except Exception as e:
            return str(e)

    @staticmethod
    def create_news(title, excerpt, description, status, news_cover_url):
        current_time = datetime.now(timezone.utc)  # Use timezone-aware datetime
        news_data = {
            "title": title,
            "excerpt": excerpt,
            "description": description,
            "status": status,
            "news_cover": news_cover_url,
            "created_at": current_time,
            "updated_at": current_time
        }
        result = news_collection.insert_one(news_data)
        news_data["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return news_data
