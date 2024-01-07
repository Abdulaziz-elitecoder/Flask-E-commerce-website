
from flask_sqlalchemy import SQLAlchemy
from flask import  url_for
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(255))  # Assuming a maximum path length of 255 characters
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    
    def __init__(self, name, image, description, price, in_stock=True,category_id=None):
        self.name = name
        self.image = image
        self.description = description
        self.price = price
        self.in_stock = in_stock
        self.category_id = category_id


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    
    products = db.relationship('Product', backref='category', lazy='dynamic')

    
    def __init__(self, name, description):
        self.name = name
        self.description = description