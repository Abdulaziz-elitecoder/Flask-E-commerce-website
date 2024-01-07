from flask_restful import fields

category_serializer={
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
}

products_serializer={
"id": fields.Integer,
"name": fields.String,
"image": fields.String,    
"description": fields.String,
"price": fields.Float,
"category": fields.Nested(category_serializer),
}


