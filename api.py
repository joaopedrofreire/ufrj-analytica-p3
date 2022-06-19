from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from numpy import require
from audiodb_api import get_album
from age import get_quote

app = Flask(__name__)
api = Api(app)

# POST age
parser1 = reqparse.RequestParser()
parser1.add_argument('name', type=str, required=True)
parser1.add_argument('birthdate', type=str, location="form", required=True)
parser1.add_argument('date', type=str, location="form", required=True)

class Age(Resource):
    def post(self):
        args = parser1.parse_args(strict=True)
        return get_quote(args)

api.add_resource(Age, '/age')

# GET album info
parser2 = reqparse.RequestParser()
parser2.add_argument('artist', type=str, location="args", required=True)

class AlbumInfo(Resource):
    def get(self):
        args = parser2.parse_args(strict=True)
        return get_album(args['artist'])

api.add_resource(AlbumInfo, '/album-info')

if __name__ == '__main__':
    app.run(debug=True)