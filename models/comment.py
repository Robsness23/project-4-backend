from app import db
from models.base import BaseModel
from models.user import UserModel

class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    # Foreign key tells me which column to point at 
    # so that every comment points to a specific plant
    # I have given FK the Primary Key of the plants table: plants.id (which extends from BaseModel)
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.id", ondelete='CASCADE'), nullable=False)

    # Adding a foreign key column to comments, with the user_id (which comes from UserModel)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    # We have to make up a new backref here for the comment users, it cannot be user because that backref exists in plant.py model
    user = db.relationship("UserModel", backref='comment_users')