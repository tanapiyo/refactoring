from stocks import Stock 
from money import MoneyManager

class VendingMachine:
    def __init__(self):
        self.stock = Stock({'coke': 5, 'diet coke': 5, 'tea': 5})
        self.money_manager = MoneyManager(5)#わかりにくい
    
    #stock探すのと、おつりに入れる
    def __check_stock(self, kindOfDrink, coin):
        if self.stock.check_stock(kindOfDrink):
            #raise ValueError("stockがありません!")
            return True
        return False
    
    def __check_charge_stock(self, coin):
        if self.money_manager.check_charge(coin):
            return True
        return False

    def __buy_drink(self, kindOfDrink, coin):
        drink = self.stock.take_from_stock(kindOfDrink)
        self.money_manager.take_from_stock_charge(coin)#ここ
        return drink

    def buy(self, coin, kindOfDrink):#処理ごとにメソッドわける
        """購入する

        Arguments:
            coin {Coin} -- 投入金額. 100円と500円のみ受け付ける.
            kindOfDrink {Enum} -- ジュースの種類.
                    コーラ({@code Juice.COKE}),ダイエットコーラ({@code Juice.DIET_COKE},お茶({@code Juice.TEA})が指定できる.
        Returns:
            Drink-- 指定したジュース. 在庫不足や釣り銭不足で買えなかった場合は {@code null} が返される.
        """
        #飲み物の在庫確認
        if not self.__check_stock(kindOfDrink, coin):
            return coin
        #釣り銭の在庫確認
        if not self.__check_charge_stock(coin):
            return coin
        #釣り銭の計算と、stockの操作
        drink = self.__buy_drink(kindOfDrink, coin)
        return drink
    

    def refund(self):
        """お釣りを取り出す

        Returns:
            int-- お釣りの金額
        """
        money = self.money_manager.get_charge()
        return money
