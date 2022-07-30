from app import db
from models.base import BaseModel


class SeasonModel(db.Model, BaseModel):
    __tablename__ = "seasons"
    season = db.Column(db.Text, nullable=True, unique=True)