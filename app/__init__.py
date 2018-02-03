from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:23456@localhost:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint
app.register_blueprint(admin_blueprint, url_prefix="/admin" )
app.register_blueprint(home_blueprint)
