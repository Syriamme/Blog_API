# helpers.py
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, BlogPost
from app import session  # Import the session directly

def create_jwt_token(user):
    access_token = create_access_token(identity=user.id)
    return access_token

def jwt_login_required(func):
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user = session.query(User).get(get_jwt_identity())
        return func(current_user, *args, **kwargs)
    return wrapper
