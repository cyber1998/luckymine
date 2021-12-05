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

    def __mine(self):
        """
        Mine an ore. It takes 3 real time seconds to mine an ore. Ores are randomly dropped.
        """
        random.seed()
        print('Starting to mine...')
        time.sleep(3)
        weights = [self.luck * weight for weight in DEFAULT_PROBABLITY.values()]
        found = random.choices(population=list(DEFAULT_PROBABLITY.keys()), weights=weights, k=1)
        print(f'You finished mining and found {object_name(found[0])}!')
        return found[0]

    def __add_to_shop(self, ore):
        """
        Add an unit of ore that you mined to your shop.
        """
        if ore not in self.inventory.keys():
            print(f'Congratulations, You found {object_name(ore)} for the first time!')
            self.inventory[ore] = 1
        else:
            print(f'Adding {object_name(ore)} to your inventory')
            self.inventory[ore] += 1
        

    def __sell_from_shop(self, ore, quantity):
        """
        Sell ores from your shop for money.
        """
        if self.inventory[ore] >= quantity:
            self.inventory[ore] -= quantity
            price = AVAILABLE_ORES[ore]
            self.money += price
            print(f'You sold {quantity} {object_name(ore)} and gained {price} coins')
            return self.quantity
        else:
            print('Not enough ores to sell')
            return None

    def __buy_asset(self, asset):
        """
        Buy an asset to increase your chances of getting better ores!
        """
        cost = AVAILABLE_ASSETS[asset]
        if self.money >= cost and asset not in self.assets:
            self.money -= cost
            self.luck *= LUCK_MULTIPLIERS[asset]
            print(f'Congratulations, you just bought the {object_name(asset)}!')
            self.assets.add(asset)
            return asset
        else:
            print(f'Not enough coins to purchase {object_name(asset)}')



    
    
