from flask import Flask
from flask_migrate import Migrate
from app.models import  db
from app.config import projectConfig as AppConfig
from flask_restful import Api
from app.products.api_views import *


def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]   # config class
    app.config['SQLALCHEMY_DATABASE_URI']=current_config.SQLALCHEMY_DATABASE_URI
    # search in the class about class variable with the given name
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)

    # init app with db instance
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    api=Api(app)
    
    api.add_resource(ProductsResourceList , '/api/products')
    api.add_resource(ProductsResource , '/api/products/<int:id>')


    #register blueprint in the application
    from app.products import product_blueprint
    app.register_blueprint(product_blueprint)

    from app.category import category_blueprint
    app.register_blueprint(category_blueprint)

    return app