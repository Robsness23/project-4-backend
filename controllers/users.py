from http import HTTPStatus

from flask import Blueprint, request
from models.user import UserModel
from serializers.user import UserSchema
from marshmallow.exceptions import ValidationError

user_schema = UserSchema()

router = Blueprint("users", __name__)

# * REGISTER a User

@router.route('/register', methods=["POST"])
def register():
    try:
        user_dictionary = request.json
        user = user_schema.load(user_dictionary)
        user.save()
        return user_schema.jsonify(user)
        # Specific error
    except ValidationError as e:
        return{"errors": e.messages, "messages": "Something went wrong"}, HTTPStatus.UNAUTHORIZED
    except Exception as e:
        return {"messages": "Something went wrong"}, HTTPStatus.UNAUTHORIZED

# * ------------------------------------------------------------------------------------- * #

# * LOGIN

@router.route('/login', methods=["POST"])
def login():
    try:
        # Get the credentials for logging in
        credentials_dictionary = request.json
        # First, grabbing the user from Postgresql by their email
        user = UserModel.query.filter_by(email=credentials_dictionary["email"]).first()
        # If there is no user registered to that email, return the below
        if not user:            
            return{"message": "No user found for this email"}, HTTPStatus.UNAUTHORIZED
        # Checking to see whether the password matches the hashed one that is stored in the db
        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "Password does not match"}, HTTPStatus.UNAUTHORIZED
        # Making a token
        token = user.generate_token()
        # Sending the token back
        return{"token": token, "message": "Welcome back!"}
    except Exception as e:
        return {"messages": "Something went wrong"}

