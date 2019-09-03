import random

class User:
    def __init__(self, name, income):
        self.__name = name
        self.__income = income
        self.__score = random.randint(1,999)
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, income):
        self.__income = income

    @property
    def score(self):
        return self.__score

    def incomeFormat(self):
        return str('{:,.2f}'.format(float(self.__income)))