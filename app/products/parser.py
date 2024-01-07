from flask_restful import reqparse

product_req_parser=reqparse.RequestParser()

product_req_parser.add_argument('name',str)
product_req_parser.add_argument('image',str)
product_req_parser.add_argument('description',str)
product_req_parser.add_argument('price',float)
product_req_parser.add_argument('category_id',int)

