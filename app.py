# app.py

from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth
from config.mongo_config import get_mongo_client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Setup JWT secret key
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
jwt = JWTManager(app)

# Initialize MongoDB client
mongo_client = get_mongo_client()

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

# Register Blueprint for authentication routes
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run()
