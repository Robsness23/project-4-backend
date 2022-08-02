# This is the controller and views for plants
# Flask's router is called Blueprint
from email.policy import HTTP
from flask import Blueprint, request, g
from app import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route
from models.plant import PlantModel
from models.comment import CommentModel
from serializers.plant import PlantSchema
from serializers.season import SeasonSchema
from serializers.pollinator import PollinatorSchema
from serializers.comment import CommentSchema


# Instantiate the plant schema
plant_schema = PlantSchema()

# Instantiate the 
season_schema = SeasonSchema()
pollinator_schema = PollinatorSchema()
comment_schema = CommentSchema()


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

# ? COMMENTS

# * POST a Comment
@router.route("/plants/<int:plant_id>/comments", methods=["POST"])
@secure_route
def create_comment(plant_id):
    comment_dictionary = request.json
    try:
        comment = comment_schema.load(comment_dictionary)
    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }
    comment.plant_id = plant_id
    comment.user_id = g.current_user.id
    comment.save()
    return comment_schema.jsonify(comment), HTTPStatus.CREATED

# * GET all comments
@router.route("/comments", methods=["GET"])
def get_all_comments():
    # * My characters live in postgres. Use SQLAlchemy to get the characters.
    comments = CommentModel.query.all() # query in an object that lives on Model.
    # query has methods like .all, to interact with the database. 

    # ? Serializing to comments json using .jsonify. many=True tells the serializer
    # ? we are giving it a list of comment models.
    return comment_schema.jsonify(comments, many=True)

# * Get 1 comment through the ID
@router.route("/comments/<int:comment_id>", methods=["GET"])
# ! Notice we are passing the character_id as an argument.
def get_single_comment(comment_id):
    comment = CommentModel.query.get(comment_id)
    # ! Empty dictionary -> boolean gives you...False
    if not comment:
      # Return a tuple with message not found and status code.
        return { "message": "Comment not found" }, HTTPStatus.NOT_FOUND
    return comment_schema.jsonify(comment)


# * Delete 1 comment through ID
@router.route("/comment/<int:comment_id>/", methods=["DELETE"])
@secure_route
def delete_comment(comment_id):
    comment = CommentModel.query.get(comment_id)
    existing_comment = CommentModel.query.get(comment_id)
    # ! Add this check whenever we want to make sure the character is the user's character that they're trying to update/delete
    if not g.current_user.id == existing_comment.user_id:
        return {"message": "Not your comment to delete!"}, HTTPStatus.UNAUTHORIZED
    db.session.delete(comment)
    db.session.commit()
    return comment_schema.jsonify(comment), HTTPStatus.NO_CONTENT


# * PUT For Comments
@router.route("/comment/<int:comment_id>", methods=["PUT"])
@secure_route
def update_comment(comment_id):
    comment_dictionary = request.json
    existing_comment = CommentModel.query.get(comment_id)
    if not existing_comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND
    # ! Add this check whenever we want to make sure the comment is the user's comment that they're trying to update/delete
    if not g.current_user.id == existing_comment.user_id:
        return {"message": "Not your comment to alter!"}, HTTPStatus.UNAUTHORIZED
    try:
        comment = comment_schema.load(comment_dictionary, instance=existing_comment, partial=True)
    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}
    comment.save()
    return comment_schema.jsonify(comment), HTTPStatus.OK

