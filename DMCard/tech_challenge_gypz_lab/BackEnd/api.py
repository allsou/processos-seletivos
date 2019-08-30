from flask import Flask
from flask_restful import Api, Resource
from resources.cardRequestResources import CardRequestResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CardRequestResource, '/cardrequest/')

if __name__ == '__main__':
    app.run(debug=True)