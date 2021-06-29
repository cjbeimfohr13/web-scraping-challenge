from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# create mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


@app.route('/')
def home():
    
    mars_data = mongo.db.marsdb.find_one()
    
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():
    mars=mongo.db.marsdb
    scrape_mars_data = scrape_mars.scrape_all()
    mars.update({}, scrape_mars_data, upsert=True)
    
    return "scrape complete"

    
if __name__ == "__main__":
    app.run(debug=True)
