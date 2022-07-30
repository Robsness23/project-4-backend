from app import db
from models.base import BaseModel


class PollinatorModel(db.Model, BaseModel):
    __tablename__ = "pollinators"
    type = db.Column(db.Text, nullable=True, unique=True)