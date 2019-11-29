from unittest import TestCase
from vending.vending import Drink, VendingMachine

class TestVendingMachine(TestCase):
  def test_buy(self):
    vm = VendingMachine()
    return_drink = vm.buy(100, 0)
    self.assertEqual(return_drink.kind, 0)
  
  def test_refund(self):
    vm2 = VendingMachine()
    vm2.buy(500, 0)
    self.assertEqual(vm2.refund(), 400)
