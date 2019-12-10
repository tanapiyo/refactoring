from drinks import DrinkCoke, DrinkDietCoke, DrinkTea, KindOfDrink

class Stock():
    def __init__(self, stock_dict):
        self.stock = stock_dict

    def check_stock(self, kindOfDrink):
        if self.stock[kindOfDrink] == 0:
            return False
        return True
    
    def take_from_stock(self, kindOfDrink):
        self.stock[kindOfDrink] = self.stock[kindOfDrink]-1
        if kindOfDrink == KindOfDrink.COKE:
            return DrinkCoke()
        if kindOfDrink == KindOfDrink.DIETCOKE:
            return DrinkDietCoke()
        if kindOfDrink == KindOfDrink.TEA:
            return DrinkTea()
    

# class StockCoke(Stock):
#     def __init__(self, stock_num):
#         super().__init__(stock_num)
#         for i in range(stock_num):
#             self.stock.append(DrinkCoke())
#         self.price = DrinkCoke.price
    
# class StockDietCoke(Stock):
#     def __init__(self, stock_num):
#         super().__init__(stock_num)
#         for i in range(stock_num):
#             self.stock.append(DrinkDietCoke())
#         self.price = DrinkDietCoke.price

# class StockTea(Stock):
#     def __init__(self, stock_num):
#         super().__init__(stock_num)
#         for i in range(stock_num):
#             self.stock.append(DrinkTea())
#         self.price = DrinkTea.price