from flask import Flask, render_template
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

@app.route("/search", methods=["POST"])
def search_results():
    return render_template("search_results.html")


@app.route("/")
def home():
    return render_template("home.html")

 



if __name__ == "__main__":
    app.run(debug=True)

