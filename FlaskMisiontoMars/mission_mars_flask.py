#Dependencies
from flask import Flask, render_template
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)


@app.route("/")
def index():
    news = mongo.db.news.find({})
    hemis = mongo.db.hemis.find({})
    wea = mongo.db.weather.find({})
    fact1 = mongo.db.facts.find({})
    values = []
    for fact in fact1:
        values.append(list(fact.values()))
    val1 = values[0][1:]
    val2 = values[1][1:]
    algo = {'val1':val1,'val2':val2}
    return render_template("index.html", news = news, hemis = hemis, wea = wea, algo = algo)


if __name__ == "__main__":
    app.run(debug=True)