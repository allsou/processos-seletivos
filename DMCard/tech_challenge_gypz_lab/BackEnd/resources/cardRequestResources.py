from flask import request, jsonify
from flask_restful import Resource,abort,reqparse
from models.user import User
from models.cardRequest import CardRequest
import json

data={
    'name' : 'Teste',
    'income' : '5151.54'
    }

inicialData = [
    {
        "req_id": 1,
        "data": 
            {
                "user": 
                {
                    "name" : "Allan Santos",
                    "income" : 1982.54,
                    "score" : 739
                },
                "status" : True,
                "credit" : 1000
            }
    }
]

'''
response = post("http://127.0.0.1:5000/cardrequest/", data = { 'name' : 'Allan', 'income' : '1231'})
response = get("http://127.0.0.1:5000/cardrequest/")
'''
#parser = reqparse.RequestParser()
#parser.add_argument('req')

def abort_if_doesnt_exist(req_id):
    if req_id not in inicialData:
        abort(404, message="Requisição {} não existe".format(req_id))

class CardRequestResource(Resource):
    def get(self):
        data_return = json.dumps(inicialData)
        data_return = json.loads(data_return)
        return data_return

    def post(self):
        #try:
        print(len(inicialData)+1)
        new_user_req = User(request.form['name'],request.form['income'])
        new_req = CardRequest(new_user_req, len(inicialData)+1)
        new_req.approvation()
        if(new_req.status):
            new_req.creditAllowed()
            inicialData.append(new_req.to_json())
        else:
            print(new_user_req.score)
            inicialData.append(new_req.to_json())
            return {'message': 'Cŕedito não aprovado.'}, 200
        
        print(request.form['income'] + ' ' + request.form['name'])
        return {'message': 'Requisição criada com sucesso!'}, 201

        #except:
        #    return 'Ocorreu um problema no cadastro de uma nova requisição!', 400
        
        #args = parser.parse_args()
        #task = {'req': args['req']}
        #inicialData[req_id] = task

    def delete(self):
        #abort_if_doesnt_exist(param)
        #del inicialData[param]
        return '', 204