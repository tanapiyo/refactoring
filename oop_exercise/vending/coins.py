from abc import ABCMeta, abstractmethod
class Coin(metaclass=ABCMeta):
    pass

class Coin100(Coin):
    def __init__(self):
        self.amount = 100

class Coin500(Coin):
    def __init__(self):
        self.amount = 100

