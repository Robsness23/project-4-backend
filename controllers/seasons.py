from http import HTTPStatus
from http.client import OK
from flask import Blueprint, request
from models.season import SeasonModel
from serializers.season import SeasonSchema

season_schema = SeasonSchema()

router = Blueprint("seasons", __name__)

@router.route("/seasons", methods=["GET"])
def get_seasons():
    seasons = SeasonModel.query.all()

    return season_schema.jsonify(seasons, many=True), HTTPStatus.OK

@router.route("/seasons/<int:season_id>", methods=["GET"])
def get_single_season(season_id):
    season = SeasonModel.query.get(season_id)

    if not season:
        return { "message": "Season not found" }, HTTPStatus.NOT_FOUND
    return season_schema.jsonify(season), HTTPStatus.OK
    