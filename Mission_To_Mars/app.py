from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)


# Set route
@app.route('/')


if __name__ == "__main__":
    app.run(debug=True)
