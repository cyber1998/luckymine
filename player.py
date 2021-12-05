import random
import time
from constants import AVAILABLE_ORES, AVAILABLE_ASSETS, LUCK_MULTIPLIERS, DEFAULT_PROBABLITY
from utils import object_name

class Player(object):

    def __init__(self, name=None):
        self.name = 'Player 1' if name is None else name
        self.__assets = set()
        self.__money = 0
        self.__luck = 1
        self.__inventory = dict()
    
    def get_account_balance(self):
        return self.__money

    def get_assets(self):
        return self.__assets

    def get_inventory(self):
        return self.__inventory

    def mine(self):
        """
        Mine an ore. It takes 3 real time seconds to mine an ore. Ores are randomly dropped.
        """
        random.seed()
        print('Starting to mine...')
        time.sleep(3)
        weights = [self.__luck * weight for weight in DEFAULT_PROBABLITY.values()]
        found = random.choices(population=list(DEFAULT_PROBABLITY.keys()), weights=weights, k=1)
        self.add_to_shop(found[0])
        print(f'You finished mining and found {object_name(found[0])}!')
        return found[0]

    def add_to_shop(self, ore):
        """
        Add an unit of ore that you mined to your shop.
        """
        if ore not in self.__inventory.keys():
            print(f'Congratulations, You found {object_name(ore)} for the first time!')
            self.__inventory[ore] = 1
        else:
            print(f'Adding {object_name(ore)} to your inventory')
            self.__inventory[ore] += 1
        

    def sell_from_shop(self, ore, quantity):
        """
        Sell ores from your shop for money.
        """
        if self.__inventory[ore] >= quantity:
            self.__inventory[ore] -= quantity
            price = AVAILABLE_ORES[ore]
            self.__money += price
            print(f'You sold {quantity} {object_name(ore)} and gained {price} coins')
            return quantity
        else:
            print('Not enough ores to sell')
            return None

    def buy_asset(self, asset):
        """
        Buy an asset to increase your chances of getting better ores!
        """
        cost = AVAILABLE_ASSETS[asset]
        if self.__money >= cost and asset not in self.__assets:
            self.__money -= cost
            self.__luck *= LUCK_MULTIPLIERS[asset]
            print(f'Congratulations, you just bought the {object_name(asset)}!')
            self.__assets.add(asset)
            return asset
        else:
            print(f'Not enough coins to purchase {object_name(asset)}')



    
    
