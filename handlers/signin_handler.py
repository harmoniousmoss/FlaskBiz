# handlers/signin_handler.py

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

    access_token = create_access_token(identity=user["email"], expires_delta=timedelta(hours=1))
    
    return jsonify(access_token=access_token), 200
