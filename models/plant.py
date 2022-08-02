from app import db
from models.base import BaseModel
from models.plant_season import plant_season
from models.season import SeasonModel
from models.pollinator import PollinatorModel
from models.plant_pollinator import plant_pollinator
from models.comment import CommentModel
from models.user import UserModel

# PollinatorModel extends BaseModel 
# It also extends db.Model 
# Extending dd.Model lets FSQLAlchemy 'know' about our model, so it can use it.

class PlantModel(db.Model, BaseModel):
    # This will be used directly to make a table in Postgresql
    __tablename__ = "plants"

    # The specific columns for the Pollinators Table
    name = db.Column(db.Text, nullable=False, unique=True)
    latinName = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False, unique=True)

    # I need to add a foreign key column to plants, with user_id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=True)

    # Here I am letting FSQLAlchemy know about the new table for seasons, I am also telling it about the JOIN table: plant_season
    seasons = db.relationship('SeasonModel', backref='seasons', secondary=plant_season)
    # Here I am letting FSQLAlchemy know about the new table for pollinators, I am also telling it about the JOIN table: plant_pollinator
    pollinators = db.relationship('PollinatorModel', backref='pollinators', secondary=plant_pollinator)

    # The below line is for serialization. It tells our comment about our plant model.
    # This is the code that associates the two models together
    # It won't make a new column, but instead specifies a relationship between the two models.
    # ? back ref should be the table name of this current table.
    comments = db.relationship('CommentModel', backref='comments', cascade="all, delete")
    # Add a user relationship to plants
    user = db.relationship('UserModel', backref='users')




