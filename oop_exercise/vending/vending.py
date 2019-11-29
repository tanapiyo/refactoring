from abc import ABCMeta, abstractmethod
from enum import Enum
import dataclasses

class KindOfDrink(Enum):#選択肢の見せ方？とstock_cokeとかほんとは紐づけたい
    COKE = "coke"
    DIETCOKE = "diet_coke"
    TEA = "tea"

class Drink(metaclass=ABCMeta):
    pass

@dataclasses.dataclass
class DrinkCoke(Drink):
    price:int = 100

@dataclasses.dataclass
class DrinkDietCoke(Drink):
    price:int = 100

@dataclasses.dataclass
class DrinkTea(Drink):
    price:int = 100

class Stock(metaclass=ABCMeta):
    def __init__(self, stock_num):
        self.stock = []

    def check_stock(self):
        if not self.stock:
            return False
        return True
    
    def take_from_stock(self):
        return self.stock.pop
    

class StockCoke(Stock):
    def __init__(self, stock_num):
        super().__init__(stock_num)
        for i in range(stock_num):
            self.stock.append(DrinkCoke())
        self.price = DrinkCoke.price
    
class StockDietCoke(Stock):
    def __init__(self, stock_num):
        super().__init__(stock_num)
        for i in range(stock_num):
            self.stock.append(DrinkDietCoke())
        self.price = DrinkDietCoke.price

class StockTea(Stock):
    def __init__(self, stock_num):
        super().__init__(stock_num)
        for i in range(stock_num):
            self.stock.append(DrinkTea())
        self.price = DrinkTea.price

class StockCharge():#100円玉の管理
    def __init__(self, coin100_num):#100円の枚数だとちょっと拡張性ないかも（Charge100つくる？）
        self.charge = []
        self.coin_factory = CoinFactory()
        for i in range(coin100_num):
            self.charge.append(self.coin_factory.get_one_coin_100())
    
    def get_quantity_of_coins(self):
        print(self.charge)
        return len(self.charge)
    
    def charge_coins(self, coins):
        for coin in coins:
            self.charge.append(coin)

class Charge():
    def __init__(self):
        self.amount =[]
    
    def add_charge(self,coin):
        self.amount.append(coin)
    
    def get_amout_of_charge(self):
        all_amount = 0
        for coin in self.amount:
            all_amount += coin.amount
        return all_amount
    
    def reset_charge(self):
        self.amount = []


class Coin(metaclass=ABCMeta):
    pass

class Coin100(Coin):
    def __init__(self):
        self.amount = 100

class Coin500(Coin):
    def __init__(self):
        self.amount = 100

class CoinFactory():
    def get_coins(self, amount):
        coinlist = []
        if amount>=500:
            coinlist.append(self.__get_coin500(amount))
            amount = amount-len(coinlist)
        coinlist.append(self.__get_coin100(amount))
        return coinlist
        
    def __get_coin100(self,amount):
        return_100_coins = []
        for i in range(amount, 100):
            return_100_coins.append(Coin100())
        return return_100_coins

    def __get_coin500(self,amount):
        return_500_coins = []
        for i in range(amount, 500):
            return_500_coins.append(Coin500())
        return return_500_coins
    
    def get_one_coin_100(self):
        return Coin100()
    
    def get_one_coin_500(self):
        return Coin500()


class VendingMachine:
    def __init__(self):
        self.stock_coke = StockCoke(5)
        self.stock_diet_coke = StockDietCoke(5)
        self.stock_tea = StockTea(5)
        self.stock_charge = StockCharge(10)
        self.charge = Charge()
        self.coin_factory = CoinFactory()
    
    #ほしいっていわれたstockについて考えるので変数に入れる
    def __get_stock_instance(self,kindOfDrink):
        if kindOfDrink == KindOfDrink.COKE:
            return self.stock_coke
        if kindOfDrink == KindOfDrink.DIETCOKE:
            return self.stock_diet_coke
        if kindOfDrink == KindOfDrink.TEA:
            return self.stock_tea
    
    #stock探すのと、おつりに入れる
    def __check_stock(self, stock, coin):
        if not stock.check_stock():
            self.charge.add_charge(coin)
            raise ValueError("stockがありません!")
    
    def __check_charge_stock(self, coin):
        if self.stock_charge.get_quantity_of_coins == 0:
            self.charge.add_charge(coin)
            raise ValueError("釣り銭が足りません!")

    def __charge_coins(self, stock, coin):
        charge = coin.amount - stock.price#この金額でcoinにしたい
        self.stock_charge.charge_coins(self.coin_factory.get_coins(charge))#釣り銭をstockに登録
        return charge#お釣りの金額をかえす


    def buy(self, coin, kindOfDrink):#処理ごとにメソッドわける
        """購入する

        Arguments:
            coin {Coin} -- 投入金額. 100円と500円のみ受け付ける.
            kindOfDrink {Enum} -- ジュースの種類.
                    コーラ({@code Juice.COKE}),ダイエットコーラ({@code Juice.DIET_COKE},お茶({@code Juice.TEA})が指定できる.
        Returns:
            Drink-- 指定したジュース. 在庫不足や釣り銭不足で買えなかった場合は {@code null} が返される.
        """
        #stockに対象のインスタンスをセットする
        stock = self.__get_stock_instance(kindOfDrink)
        #飲み物の在庫確認
        self.__check_stock(stock, coin)
        #釣り銭の在庫確認
        self.__check_charge_stock(coin)
        #釣り銭の計算と、stockの操作
        self.__charge_coins(stock, coin)
        #かったからstockけす
        drink = stock.take_from_stock()
        return drink
    

    def refund(self):
        """お釣りを取り出す

        Returns:
            int-- お釣りの金額
        """
        result = self.charge.get_amout_of_charge()
        self.charge.reset_charge()
        return result
