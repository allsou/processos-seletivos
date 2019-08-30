from flask import request, jsonify
from flask_restful import Resource,abort,reqparse
from models.user import User
from models.cardRequest import CardRequest
import json

data={
    'name' : 'Teste',
    'income' : '5151.54'
    }

inicialData = {
    'req1': 
        {
            'user': 
            {
                'name' : 'Allan Santos',
                'income' : '1982.54',
                'score' : '739',
            },
        'status' : 'True',
        'credit' : '1000',
        },
}

#jsontext = json.loads(inicialData)

#parser = reqparse.RequestParser()
#parser.add_argument('req')

def abort_if_doesnt_exist(param):
    if param not in inicialData:
        abort(404, message="Requisição {} não existe".format(param))

class CardRequestResource(Resource):
    def get(self):
        return inicialData

    def post(self):
        #try:
        new_user_req = User(request.form['name'],request.form['income'])
        new_req = CardRequest(new_user_req)
        new_req.approvation()
        if(new_req.status):
            new_req.creditAllowed()
        else:
            print(new_user_req.score)
            return {'message': 'Cŕedito não aprovado.'}, 200
        print(new_req.credit)
        print(new_req.user.score)
        #print(jsonify(new_req))
        print(request.form['income'] + ' ' + request.form['name'])
        return 'task', 201

        #except:
        #    return 'Ocorreu um problema no cadastro de uma nova requisição!', 400
        
        #args = parser.parse_args()
        #task = {'req': args['req']}
        #inicialData[req_id] = task

    def delete(self):
        #abort_if_doesnt_exist(param)
        #del inicialData[param]
        return '', 204