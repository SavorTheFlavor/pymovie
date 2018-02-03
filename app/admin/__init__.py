from flask import Blueprint

admin = Blueprint("admin", __name__)  # blueprint name and this module name
# this import statement must be here, otherwise in views.py file, import statement failed cause the undefinition of 'admin'
import app.admin.views
