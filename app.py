# * Hello world flask app.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.environment import db_URI


# ? Instantiate flask
# ? __name__ is going to be a different value depending on
# ? where you run flask from. If you run this directly,
# ? it will be '__main__'
app = Flask(__name__)

# Configuring it with flask
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
# Removes a warning for an unused part of the library
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Plugging in a Flask SQLAlchemy. This is an important line, SQLAlchemy is a class. (app) is an object that we are passing to SQLAlchemy.
# This is telling Flask SQLAlchemy where the db lives on our system
db = SQLAlchemy(app)

# ? Make a very basic route to talk to...
# * This @ syntax is a 'Decorator'. This decorator tell us
# * Which route our function belong to (our path for this route)
@app.route("/hello")
def home():
    return { "hello": "world" }
