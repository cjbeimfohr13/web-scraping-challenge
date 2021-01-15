from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

conn = 'mongodb://localhost:'

client = pymongo.MongoClient(conn)

@app.route('/')
def index():
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scraper():
    mission_to_mars.scrape()
    return()

    
if __name__ == "__main__":
    app.run(debug=True)
