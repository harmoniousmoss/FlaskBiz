# routes/contact_routes.py

from flask import Blueprint
from handlers.contact_handler import post_contact

contact = Blueprint('contact', __name__)

contact.route('/api/v1/contact', methods=['POST'])(post_contact)
