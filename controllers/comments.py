from http import HTTPStatus
from flask import Blueprint, request, g
from models.comment import CommentModel
from serializers.comment import CommentSchema
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route
from app import db


# Instantiate the schema
comment_schema = CommentSchema()

# Instantiate the router
# This take, __name__, and a unique name to register
router = Blueprint("comments", __name__)

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