from app import db

# Here I am creating a Join Table, using SQLAlchemy
plant_pollinator = db.Table('plant_pollinators',
    # Here we define our 2 columns, just like SQL 
    db.Column('plant_id', db.Integer, db.ForeignKey('plants.id'), primary_key=True),
    db.Column('pollinator_id', db.Integer, db.ForeignKey('pollinators.id'), primary_key=True)
)