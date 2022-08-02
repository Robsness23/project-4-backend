# * Hello world flask app.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.environment import db_URI
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt


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

# Instantiating Marshmallow framework
ma = Marshmallow(app)

# Instantiating my Bcrypt class
bcrypt = Bcrypt(app)

# Import controllers so that I can register it and prefix it with "/api"
from controllers import plants, users

app.register_blueprint(plants.router, url_prefix="/api")
# app.register_blueprint(seasons.router, url_prefix="/api")
# app.register_blueprint(pollinators.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")