"""
Vending Machine一共有三种状态：NoSelection, HasSelection, InsertedMoney
Vending Machine一共卖三种饮料：Coke, Sprite和MountainDew
要求Vending Machine在正确的状态要有正确的输出
"""

from enum import Enum
from abc import ABCMeta, abstractclassmethod


class State(ABCMeta):
    @abstractclassmethod
    def select_item(self, drink: Drink):
        pass

    @abstractclassmethod
    def insert_money(self, value):
        pass
    
    @abstractclassmethod
    def cancle(self):
        pass

    @abstractclassmethod
    def execute(self):
        pass


class NoSelection(object, State):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


class Drink(Enum):
    coke = 0
    sprite = 1
    mountain_dew = 2


# class VendingMachine(object):
