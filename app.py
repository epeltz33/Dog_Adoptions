from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from modules.user import user_blueprint
from modules.search import search_blueprint
import os

load_dotenv() # load environment variables from .env file

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.register_blueprint(user_blueprint)
app.register_blueprint(search_blueprint)


mongo = PyMongo(app)

# other routes here




if __name__ == "__main__":
    app.run(debug=True)

