from app import ma
from models.plant import PlantModel
from marshmallow import fields

# Here I am going to extend the Marshmallow serializer schema
# It is a schema which serializes:
# Python Model -> JSON
# Python dictionary -> Python Model

class PlantSchema(ma.SQLAlchemyAutoSchema):
    # then pop a nested class called Meta
    class Meta:
        model = PlantModel
        load_instance = True
        # Within the Meta class here I am telling it about my model which I want to be able to serialize things on
        # Basically it tells Marshmallow to give me back a Model when I deserialize, rather than a dictionary
    comments = fields.Nested("CommentSchema", many=True)
    seasons = fields.Nested("SeasonSchema", many=True)
    pollinators = fields.Nested("PollinatorSchema", many=True)
    user = fields.Nested("UserSchema", many=False)