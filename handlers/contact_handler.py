# handlers/contact_handler.py

from flask import request, jsonify
from wtforms import Form, StringField, validators
from models.contact_model import Contact
import re

class ContactForm(Form):
    full_name = StringField('Full Name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    phone_number = StringField('Phone Number', [validators.Optional()])
    message = StringField('Message', [validators.DataRequired()])

def validate_phone_number(phone_number):
    # Validates the phone number format +628114519459
    pattern = r'^\+62\d{9,15}$'
    if phone_number and not re.match(pattern, phone_number):
        return False
    return True

def post_contact():
    data = request.get_json()  # Parse JSON data from the request
    form = ContactForm(data=data)  # Use the 'data' parameter to pass in the JSON

    if not form.validate():
        return jsonify({"msg": "Validation failed", "errors": form.errors}), 400

    phone_number = form.phone_number.data
    if phone_number and not validate_phone_number(phone_number):
        return jsonify({"msg": "Invalid phone number format"}), 400

    # Create the contact
    contact = Contact.create_contact(
        full_name=form.full_name.data,
        email=form.email.data,
        phone_number=phone_number,
        message=form.message.data
    )
    
    # Return success message and the submitted data
    return jsonify({
        "msg": "Contact submission successful",
        "contact": contact
    }), 201
