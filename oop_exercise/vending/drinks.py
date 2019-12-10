from enum import Enum
from abc import ABCMeta, abstractmethod
import dataclasses

class KindOfDrink(Enum):#選択肢の見せ方？とstock_cokeとかほんとは紐づけたい
    COKE = "coke"
    DIETCOKE = "diet coke"
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
