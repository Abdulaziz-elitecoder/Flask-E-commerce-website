from flask import  Blueprint
category_blueprint= Blueprint('category', __name__, url_prefix='')
from app.category import views