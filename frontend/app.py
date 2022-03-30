import flask
from flask_pymongo import PyMongo


app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/cooker")
db = mongodb_client.db

@app.route("/")
def home():
    todos = db.recipes.find({},{'_id': 0})
    return flask.render_template("dashboard.html")

if __name__ == "__main__":
    app.run()