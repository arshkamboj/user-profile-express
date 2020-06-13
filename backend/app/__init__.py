from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///users.db'
#'mysql+pymysql://root:root@localhost:3306/users'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

CORS(app)

# initialize
jwt = JWTManager(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

from . import routes

