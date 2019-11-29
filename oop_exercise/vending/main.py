from vending import VendingMachine, CoinFactory, KindOfDrink

def main():
  coin_factory = CoinFactory()
  coin100 = coin_factory.get_one_coin_100()
  #coin500 = coin_factory.get_one_coin_500()
  vending_machine = VendingMachine()
  drink = vending_machine.buy(coin100,KindOfDrink.COKE)
  charge = vending_machine.refund()

  print("bought", drink)
  print("charge is ", charge)
  print(str(drink))

if __name__ == "__main__":
  main()

