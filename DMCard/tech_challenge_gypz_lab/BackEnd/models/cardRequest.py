from models.user import User
from flask_restful import Resource

class CardRequest:

    def __init__(self, User):
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

    def approvation(self):
        if(self.__user.score > 299):
            self.__status = True

    def creditAllowed(self):
        if(self.__user.score >= 300 and self.__user.score <= 599):
            self.__credit = 1000

        elif(self.__user.score <= 799):
            if(float(self.__user.income)*0.5 < 1000):
                self.__credit = 1000
            else:
                self.__credit = float(self.__user.income)*0.5

        elif(self.__user.score <= 950):
            self.__credit = float(self.__user.income)*2

        elif(self.__user.score <= 999):
            self.__credit = 1000000
    