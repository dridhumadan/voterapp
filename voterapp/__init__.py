from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://app:app123@localhost/dbms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)

from voterapp.errors.handlers import errors
from voterapp.home.routes import home
from voterapp.auth.routes import auth
from voterapp.users.routes import users

app.register_blueprint(errors)
app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(users)
