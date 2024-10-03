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
    # Retrieve the user's identity (which now includes both full name and email)
    user_identity = get_jwt_identity()
    user_full_name = user_identity["full_name"]  # Get the full name from the JWT

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

    # Create the news post and associate it with the user's full name
    news = News.create_news(
        title=form.title.data,
        excerpt=form.excerpt.data,
        description=form.description.data,
        status=form.status.data,
        news_cover_url=news_cover_url
    )

    # Return success message and the submitted data
    return jsonify({
        "msg": "News posted successfully",
        "news": news,
        "posted_by": user_full_name  # Display the full name instead of email
    }), 201
