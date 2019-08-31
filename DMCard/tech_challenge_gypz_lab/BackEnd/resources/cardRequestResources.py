from flask import request, jsonify
from flask_restful import Resource,abort,reqparse
from models.user import User
from models.cardRequest import CardRequest
import json

data={
    'name' : 'Teste',
    'income' : '5151.54'
    }

inicialData = [{"req_id": 1,"data":{"user":{"name" : "Allan Santos","income" : 1982.54,"score" : 739},"status" : True,"credit" : 1000}}]

'''
response = post("http://127.0.0.1:5000/cardrequest", data = { 'name' : 'Allan', 'income' : '1231'})
response = get("http://127.0.0.1:5000/cardrequest")
response = delete("http://127.0.0.1:5000/cardrequest/1")
'''

class CardRequestResource(Resource):
    def get(self):
        data_return = json.dumps(inicialData)
        data_return = json.loads(data_return)
        return data_return, 200

    def post(self):
        try:
            new_user_req = User(request.form['name'],request.form['income'])
            new_req = CardRequest(new_user_req, len(inicialData)+1)
            new_req.approvation()
            if(new_req.status):
                new_req.creditAllowed()
                inicialData.append(new_req.to_json())
            else:
                print(new_user_req.score)
                inicialData.append(new_req.to_json())
                return [{"message": "Cŕedito não aprovado."}], 200
            
            print(request.form['income'] + ' ' + request.form['name'])
            return [{"message": "Requisição {} criada com sucesso!".format(new_req.req_id)}], 201
        except:
            return [{"message" : "Requisição não existe foi criada, verificar nome e renda"}], 404

class CardRequestMaintenceResource(Resource):
    def delete(self, req_id):
        try:
            for data in inicialData:
                if(data["req_id"] == req_id):
                    inicialData.remove(data)
            return "Requisição {} excluída com sucesso".format(req_id), 204
        except:
            return [{"message" : "Requisição {} não existe".format(req_id)}], 404