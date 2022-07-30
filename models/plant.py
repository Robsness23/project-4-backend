from app import db
from models.base import BaseModel
from models.plant_season import plant_season
from models.season import SeasonModel
from models.pollinator import PollinatorModel
from models.plant_pollinator import plant_pollinator

# PollinatorModel extends BaseModel 
# It also extends db.Model 
# Extending dd.Model lets FSQLAlchemy 'know' about our model, so it can use it.

class PlantModel(db.Model, BaseModel):
    # This will be used directy to make a table in Postgresql
    __tablename__ = "plants"

    # The specific columns for the Pollinators Table
    name = db.Column(db.Text, nullable=False, unique=True)
    latinName = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    seasons = db.relationship('SeasonModel', backref='seasons', secondary=plant_season)
    attracts = db.relationship('PollinatorModel', backref='pollinators', secondary=plant_pollinator)
    image = db.Column(db.Text, nullable=False, unique=True)


# TO DO :
# 1. Users
# 2. Comments



