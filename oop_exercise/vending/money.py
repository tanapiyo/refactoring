class MoneyManager():
    def __init__(self, coin100_num):
        self.__stock_charge = StockCharge(coin100_num)
        self.__charge = Charge()
    
    def check_charge(self, coin):#おつり足りてるか
      return self.__stock_charge.check_charge(coin)

    def take_from_stock_charge(self, coin):#問答無用で100円で買う
      self.__stock_charge.take_from_stock_charge(coin)
      self.__charge.add_charge(coin)

    def get_charge(self):
      return self.__charge.amount

class StockCharge():#100円玉の管理
    def __init__(self, coin100_num):
        self.charge = {'coin100': coin100_num, 'coin500': 0}
    
    def check_charge(self, coin):
      if self.charge['coin100'] == 0:
        return False
      if coin.amount == 500:
        return self.charge['coin100'] >= 4
    
    def take_from_stock_charge(self, coin):
      if coin.amount == 100:
        self.charge['coin100'] = self.charge['coin100']-1
        return None
      if coin.amount == 500:
        self.charge['coin100'] = self.charge['coin100']-4
        self.charge['coin500'] = self.charge['coin500']+1
        return None
      
    
class Charge():#価値で管理
    def __init__(self):
        self.amount = 0
    
    def add_charge(self,coin):
      self.amount += coin.amount -100#100円買ったのでひく
    