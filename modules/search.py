from flask import Blueprint, render_template

search_blueprint = Blueprint("search", __name__, url_prefix="/search") 




@search_blueprint.route("/search")
def search_results():
    return render_template("search_results.html")

