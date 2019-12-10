from vending import VendingMachine
from drinks import KindOfDrink
from coins import Coin100, Coin500

def main():
  coin100 =Coin100()
  coin500 = Coin500()
  vending_machine = VendingMachine()
  drink = vending_machine.buy(coin100,KindOfDrink.COKE)
  charge = vending_machine.refund()

  print("bought", drink)
  print("charge is ", charge)
  print(str(drink))

if __name__ == "__main__":
  main()

