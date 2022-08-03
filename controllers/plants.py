# This is the controller and views for plants
# Flask's router is called Blueprint
from email.policy import HTTP
from flask import Blueprint, request, g
from app import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route
from models.plant import PlantModel
from serializers.plant import PlantSchema

# Instantiate the plant schema
plant_schema = PlantSchema()

# Instantiate the router
# This take, __name__, and a unique name to register
router = Blueprint("plants", __name__)


# * ------------------------------------------------------------------------------------------------------- • #

# ? PLANTS 

# GET all the plants
@router.route("/plants", methods=["GET"])
def get_plants():
    # * All my plants live in postgresql. I will use SQLAlchemy to get the plants.
    plants = PlantModel.query.all() # here I am querying an object that lives on Model

    # ? Serializing to plants json using .jsonify, many=True tells the serializer
    # ? that we are giving it a list of plant models.
    return plant_schema.jsonify(plants, many=True), HTTPStatus.OK


# ? <TYPE:PARAM_NAME>
# ? TYPE is your type, e.g. int
# ? PARAM_NAME is your parameter
# GET 1 plant through the ID 
@router.route("/plants/<int:plant_id>", methods=["GET"])
# I pass the plant_id as an argument
def get_single_plant(plant_id):
    plant = PlantModel.query.get(plant_id)
    # Empty dictionary -> boolean gives you...False
    if not plant:
        return {"message": "Plant not found"}, HTTPStatus.NOT_FOUND
    return plant_schema.jsonify(plant), HTTPStatus.OK


# POST a plant 
@router.route("/plants", methods=["POST"])
@secure_route
def create_plant():
    plant_dictionary = request.json
    # * Turning this dictionary -> PlantModel
    # * This could cause Validation Error, so I'm try excepting
    try:
        # * .load will deserialize dictionary -> PlantModel
        plant = plant_schema.load(plant_dictionary)
        # Using marshmallow validation error
    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }
    # Save my plants using the methods that are defined in BaseModel
    # Add a current user
    plant.user_id = g.current_user.id
    plant.save()
    jsondumps = plant_schema.dumps(plant)
    print(jsondumps, type(jsondumps))
    return plant_schema.jsonify(plant), HTTPStatus.CREATED

# PUT a plant
@router.route("/plants/<int:plant_id>", methods=["PUT"])
@secure_route
def update_plant(plant_id):
    plant_dictionary = request.json
    existing_plant = PlantModel.query.get(plant_id)
    if not existing_plant:
        return { "message": "Plant not found" }, HTTPStatus.NOT_FOUND
    if not g.current_user.id == existing_plant.user_id:
        return { "message": "Not your plant to alter" }, HTTPStatus.UNAUTHORIZED
    try: 
        plant = plant_schema.load(plant_dictionary, instance=existing_plant, partial=True)
    except ValidationError as e:
        return { "errors": e.messages, "messages": "Something went wrong" }
    plant.save()
    return plant_schema.jsonify(plant), HTTPStatus.OK

# DELETE 1 plant through ID
@router.route("/plant/<int:plant_id>", methods=["DELETE"])
@secure_route
def delete_plant(plant_id): 
    plant = PlantModel.query.get(plant_id)
    existing_plant = PlantModel.query.get(plant_id)

    if not g.current_user.id == existing_plant.user_id:
        return { "message": "Not your plant to delete" }, HTTPStatus.UNAUTHORIZED
    if not plant:
        return { "message": "Plant not found" }, HTTPStatus.NOT_FOUND
    plant.remove()
    return '', HTTPStatus.NO_CONTENT

# * ------------------------------------------------------------------------------------------------------------------------------- * #



