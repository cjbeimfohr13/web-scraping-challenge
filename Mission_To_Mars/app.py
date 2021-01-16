from flask import Flask, render_template
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

# created database mars in mongo
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

# db = client.collection(create a collection for the database mars)
mars = db.mars

@app.route('/')
def index():
    
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def scraper():
    listings = mongo.db.listings
    listings_data = scrape_craigslist.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)
    return()

    
if __name__ == "__main__":
    app.run(debug=True)
