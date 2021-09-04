from models.user import User
from flask_restful import Resource

class CardRequest:

    def __init__(self, User, id):
        self.__req_id = id
        self.__status = False
        self.__credit = 0
        self.__user = User

    @property
    def status(self):
        return self.__status

    @property
    def credit(self):
        return self.__credit
        
    @property
    def user (self):
        return self.__user

    @property
    def req_id (self):
        return self.__req_id

    def approvation(self):
        if(self.__user.score > 299):
            self.__status = True

    def creditAllowed(self):
        if(self.__user.score >= 300 and self.__user.score <= 599):
            self.__credit = 1000.00

        elif(self.__user.score <= 799):
            if(float(self.__user.income)*0.5 < 1000):
                self.__credit = 1000.00
            else:
                self.__credit = float(self.__user.income)*0.5

        elif(self.__user.score <= 950):
            self.__credit = float(self.__user.income)*2

        elif(self.__user.score <= 999):
            self.__credit = 1000000.00

    def creditFormat(self):
        return str('{:,.2f}'.format(float(self.__credit)))

    def to_json(self):
        ret = {"req_id": + self.__req_id,"data":{"user": {"name" : self.__user.name,"income" : self.__user.incomeFormat(),"score" : self.__user.score},"status" : self.__status,"credit" : self.creditFormat()}}
        return ret
    