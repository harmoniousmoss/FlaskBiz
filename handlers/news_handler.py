# handlers/news_handler.py

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.news_model import News
from wtforms import Form, StringField, SelectField, validators
from werkzeug.utils import secure_filename

class NewsForm(Form):
    title = StringField('Title', [validators.DataRequired()])
    excerpt = StringField('Excerpt', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    status = SelectField('Status', choices=[('draft', 'Draft'), ('published', 'Published')], validators=[validators.DataRequired()])

@jwt_required()
def post_news():
    # Retrieve the user identity from the JWT token
    user_identity = get_jwt_identity()

    # Parse the form data
    form = NewsForm(request.form)

    if not form.validate():
        return jsonify({"msg": "Validation failed", "errors": form.errors}), 400

    # Get the uploaded file
    news_cover = request.files.get("news_cover")

    if news_cover:
        file_name = secure_filename(news_cover.filename)
        news_cover_url = News.upload_news_cover(news_cover)
    else:
        return jsonify({"msg": "News cover is required"}), 400

    # Create the news post and associate it with the user identity
    news = News.create_news(
        title=form.title.data,
        excerpt=form.excerpt.data,
        description=form.description.data,
        status=form.status.data,
        news_cover_url=news_cover_url
    )

    # You can add the user_identity to the response to confirm association
    return jsonify({
        "msg": "News posted successfully",
        "news": news,
        "posted_by": user_identity  # Indicate who posted the news
    }), 201
