from flask_restful import Resource , marshal_with
from app.models import Product
from app import db 


from app.products.serializer import products_serializer
from app.products.parser import product_req_parser
from app.products.views import *




class ProductsResourceList(Resource):
    
    @marshal_with(products_serializer)
    def get(self):
        products = Product.query.all()
        return products
    
    @marshal_with(products_serializer)
    def post(self):
        data = product_req_parser.parse_args()
        product = Product(
            name=data['name'],
            image=data['image'],
            description=data['description'],
            price=data['price'],
            category_id=data['category_id']
        )
        db.session.add(product)
        db.session.commit()
        return product, 201
    




class ProductsResource(Resource):

    @marshal_with(products_serializer)
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        return product
    
    
    def put(self,id):
        product = Product.query.filter_by(id=id).first()
        data = product_req_parser.parse_args()
        product.name = data['name']
        product.image = data['image']
        product.description = data['description']
        product.price = data['price']
        product.category_id = data['category_id']
        db.session.commit()
        return "successfully updated"
    
    
    def delete(self,id):
        product = Product.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()
        return "Product deleted successfully"

