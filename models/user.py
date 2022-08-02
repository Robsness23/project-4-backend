from app import db, bcrypt
# Import datetime
from datetime import datetime, timedelta
from models.base import BaseModel
from sqlalchemy.ext.hybrid import hybrid_property
import jwt
from config.environment import secret



class UserModel(db.Model, BaseModel):
    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)

    password_hash = db.Column(db.Text, nullable=True)


    # I want to set a password field that doesn't save into the db for security reasons. (I never want to save the original password as data breaches do happen).
    # by adding the password_hash it will ensure that there is a password field on the model when I want to create a user
    # It is the password_hash which will be saved the the db


    @hybrid_property
    def password(self):
        print("Ignore that password")
        pass

# I am using the password function above with the hybrid_property decorator. This will be called 
# by FSQLAlchemy when the model is created, before saving to the db.

    @password.setter
    def password(self, password_plaintext):
        print("You are now inside the password hash method")
        # * The below is the code that hashes the password. It will give back an encoded password
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        # * The decoded password, that we actually want to store in the db
        self.password_hash = encoded_pw.decode("utf-8")
    
    
    # The below is using bcrypt to validate the password against the password hash that is stored in the db
    def validate_password(self, plaintext_password):
            return bcrypt.check_password_hash(self.password_hash, plaintext_password)
    
    
    def generate_token(self):
        # Creating a token for the user
        # as per jwt we need a payload
        payload = {
            "exp": datetime.utcnow() + timedelta(days=1), # * this advises when the token will expire
            "iat": datetime.utcnow(), # * this advises the issued at time/date
            "sub": self.id, # * this attaches the user id onto the token, so it can identify which user it belongs to 
        }
    
        # I now need to actually create the token.
        token = jwt.encode(
            payload,
            secret,
            algorithm="HS256"
        )
        return token
 