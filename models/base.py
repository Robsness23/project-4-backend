from app import db
from datetime import *

# ? This is the very first Flask SQLAlchemy model
# It is a class in python
# Flask SQLAlchemy will create tables based on these models
#┬áBasically, the SQL is written for you

class BaseModel:
    # This is a static field. We don't need to make an object to set this value.
    # It's a way of specifying fields that don't change in value

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # * Add a method here to save my model to the database
    def save(self):
        db.session.add(self)
        db.session.commit()
    # * Add a method here to remove
    def remove(self):
        db.session.delete(self)
        db.session.commit()