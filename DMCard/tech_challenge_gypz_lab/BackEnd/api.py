from flask import Flask, render_template
from flask_restful import Api, Resource
from resources.cardRequestResources import CardRequestMaintenceResource, CardRequestResource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def inddex():
    return render_template('index.html')

api.add_resource(CardRequestResource, '/cardrequest')
api.add_resource(CardRequestMaintenceResource, '/cardrequest/<int:req_id>')
if __name__ == '__main__':
    app.run(debug=True)