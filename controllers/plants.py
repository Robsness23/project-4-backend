# This is the controller and views for plants
# Flask's router is called Blueprint
from flask import Blueprint, request
from app import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from models.plant import PlantModel
from serializers.plant import PlantSchema

# Instantiate the plant schema
plant_schema = PlantSchema()


# Instantiate the router
# This take, __name__, and a unique name to register
router = Blueprint("plants", __name__)


# * ------------------------------------------------------------------------------------------------------- • #

# Get all the plants
@router.route("/plants", methods=["GET"])
def get_plants():
    # * All my plants live in postgresql. I will use SQLAlchemy to get the plants.
    plants = PlantModel.query.all() # here I am querying an object that lives on Model

    # ? Serializing to plants json using .jsonify, many=True tells the serializer
    # ? that we are giving it a list of plant models.
    return plant_schema.jsonify(plants, many=True), HTTPStatus.OK