from app import ma
from models.season import SeasonModel

class SeasonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SeasonModel
        load_instance = True 