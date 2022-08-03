from http import HTTPStatus
from flask import Blueprint, request
from models.pollinator import PollinatorModel
# from marshmallow.exceptions import ValidationError
from serializers.pollinator import PollinatorSchema

pollinator_schema = PollinatorSchema()

router = Blueprint("pollinators", __name__)

@router.route("/pollinators", methods=["GET"])
def get__pollinators():
    pollinators = PollinatorModel.query.all()
    return pollinator_schema.jsonify(pollinators, many=True)

@router.route("/pollinators/<int:pollinator_id>", methods=["GET"])
def get_single_pollinator(pollinator_id):
    pollinator = PollinatorModel.query.get(pollinator_id)

    if not pollinator:
        return { "message": "Pollinator not found" }, HTTPStatus.NOT_FOUND
    return pollinator_schema.jsonify(pollinator), HTTPStatus.OK


