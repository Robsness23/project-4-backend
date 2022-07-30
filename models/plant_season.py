from app import db

# Here I am creating a Join Table, using SQLAlchemy
plant_season = db.Table('plant_seasons',
    # Here we define our 2 columns, just like SQL 
    db.Column('plant_id', db.Integer, db.ForeignKey('plants.id'), primary_key=True),
    db.Column('season_id', db.Integer, db.ForeignKey('seasons.id'), primary_key=True)
)