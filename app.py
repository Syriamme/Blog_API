from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy engine and session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from routes import *

if __name__ == '__main__':
    with app.app_context():  # Using app context for database operations
        db.create_all()
    app.run(debug=True)
