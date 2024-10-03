# routes/news_routes.py

from flask import Blueprint
from handlers.news_handler import post_news

news = Blueprint('news', __name__)

news.route('/api/v1/news', methods=['POST'])(post_news)
