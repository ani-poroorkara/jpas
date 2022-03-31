import flask
from flask_pymongo import PyMongo
import pygal
from pygal.style import BlueStyle

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/JPAS")
db = mongodb_client.db

@app.route("/")
def home():

    # Pie
    graph_data_pie = get_job_count()

    # Bar
    graph_data_bar = get_job_count_bar()

    # Line
    graph_data_line = get_job_count_line()
    return flask.render_template("dashboard.html", job_count_pie = graph_data_pie, job_count_bar = graph_data_bar, job_count_line = graph_data_line)


# Line
def get_job_count_line():
    data = db.job_count.find({},{'_id': 0})
    return create_graph_line(data)

def create_graph_line(data):
    line_chart = pygal.Line(fill=True)
    for doc in data:
        line_chart.add(doc.get("name"),doc.get("count"))
    line_chart.render()
    return line_chart.render_data_uri()


# Pie
def get_job_count():
    data = db.job_count.find({},{'_id': 0})
    return create_graph_pie(data)

def create_graph_pie(data):
    pie_chart = pygal.Pie()
    for doc in data:
        pie_chart.add(doc.get("name"),doc.get("count"))
    pie_chart.render()
    return pie_chart.render_data_uri()

# Bar 
def get_job_count_bar():
    data = db.job_count.find({},{'_id': 0})
    return create_graph_bar(data)

def create_graph_bar(data):
    bar_chart = pygal.HorizontalBar()
    for doc in data:
        bar_chart.add(doc.get("name"),doc.get("count"))
    bar_chart.render()
    return bar_chart.render_data_uri()

if __name__ == "__main__":
    app.run()