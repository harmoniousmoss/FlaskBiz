# routes/auth_routes.py

from flask import Blueprint
from handlers.signin_handler import signin

auth = Blueprint('auth', __name__)

auth.route('/api/v1/signin', methods=['POST'])(signin)
