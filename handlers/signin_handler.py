from flask import request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def signin():
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    user = User.find_by_email(email)

    if not user or not User.check_password(user["password"], password):
        return jsonify({"msg": "Bad credentials"}), 401

    # Create the access token
    access_token = create_access_token(identity=user["email"], expires_delta=timedelta(hours=1))
    
    # Exclude password from user data before sending the response
    user_data = {
        "full_name": user["full_name"],
        "email": user["email"]
    }
    
    # Return both the token and the user information
    return jsonify(access_token=access_token, user=user_data), 200
