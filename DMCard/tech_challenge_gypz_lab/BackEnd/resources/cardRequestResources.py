from flask import request, jsonify
from flask_restful import Resource,abort,reqparse
from models.user import User
from models.cardRequest import CardRequest
import json
from tinydb import TinyDB, Query

db = TinyDB('./resources/db.json')
Req = Query()

#inicialData = [{"req_id": 1,"data":{"user":{"name" : "Allan Santos","income" : 1982.54,"score" : 739},"status" : True,"credit" : 1000}}]
'''
response = post("http://127.0.0.1:5000/cardrequest", data = { 'name' : 'Allan', 'income' : '1231'})
response = get("http://127.0.0.1:5000/cardrequest")
response = delete("http://127.0.0.1:5000/cardrequest/1")
'''

def lastReq(dataReq):
    if(len(dataReq) == 0):
        return 1
    value = 0
    for i in dataReq:
        if(i["req_id"] > value ):
            value = i["req_id"]
    return value+1

def retJson(data):
    data = json.dumps(data)
    data = json.loads(data)
    return data

class CardRequestResource(Resource):
    def get(self):
        data_return = json.dumps(db.all())
        data_return = json.loads(data_return)
        return data_return, 200

    def post(self):
        #try:
        income = request.json["income"]
        income = income.replace(",","")
        new_user_req = User(request.json["name"],float(income))
        new_req = CardRequest(new_user_req, lastReq(db.all()))
        new_req.approvation()
        if(new_req.status):
            new_req.creditAllowed()
            db.insert(new_req.to_json())
        else:
            db.insert(new_req.to_json())
            data = {"message": "Cŕedito não aprovado para requisição {}".format(new_req.req_id)}
            return retJson(data), 200
        data = {"message": "Requisição {} criada com sucesso!".format(new_req.req_id)}
        return retJson(data), 201
        #except:
            #data = {"message" : "Requisição não existe foi criada, verificar nome e renda"}
            #return retJson(data), 200

class CardRequestMaintenceResource(Resource):
    def delete(self, req_id):
        try:
            db.remove(Req.req_id == req_id)
            data = {"message":"Requisição {} excluída com sucesso".format(req_id)}
            return retJson(data), 200
        except:
            data = {"message" : "Requisição {} não existe".format(req_id)}
            return retJson(data), 200