from app import ma
from models.pollinator import PollinatorModel

class PollinatorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PollinatorModel
        load_instance = True 