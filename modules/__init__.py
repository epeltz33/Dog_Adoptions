from flask import Flask
from .user import user_blueprint
from .search import search_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint) 
    app.register_blueprint(search_blueprint)

    return app # return the app object to be used in app.py