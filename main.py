import pandas as pd
from constants import AVAILABLE_ASSETS
from player import Player
from utils import object_name

class Game(object):

    state = 'running'

    def __init__(self):
        self.player = None

    def create_player(self, name=None):
        player = Player(name=name)
        self.player = player
    
    def get_player(self):
        return self.player

    def get_assets(self):
        df = pd.DataFrame(list(self.player.get_assets()))
        df.columns = ["Owned Assets"]
        df.applymap(lambda x: object_name(x))
        print(df)
        return df
    
    def list_assets(self):
        df = pd.DataFrame(list(AVAILABLE_ASSETS.keys()))
        df.columns = ["Assets"]
        df.applymap(lambda x: object_name(x))
        print(df)
        return df

    def list_player_inventory(self):
        shop = self.player.get_inventory()
        if shop == {}:
            print('You have no ores mined')
            return
    
        print(f"{self.player.name}'s Shop")
        tildes = "~" * len(self.player.name) + "~~~~~"
        
        "Item Name", "Quantity"
        print(df)
        
        return len(shop)
        
    def display_available_commands(self):
        print('Available commands: ')
        print('1. mine')
        print('2. balance')
        print('3. close')
        print('4. buy')
        print('5. sell')

if __name__ == '__main__':
    g = Game()
    g.create_player("Cyber")
    player = g.get_player()

    while g.state == 'running':
        g.display_available_commands()
        command = input('Enter command: ')
        if command.lower() == 'mine':
            player.mine()
        elif command.lower() == 'balance':
            balance = player.get_account_balance()
            print(balance)
        elif command.lower() == 'close':
            g.state = 'not running'
        elif command.lower() == 'buy':
            g.list_assets()
            asset_to_buy = input("Enter the name of the asset you want to buy: ")
            player.buy_asset(asset_to_buy)
        elif command.lower() == 'sell':
            available_items = g.list_player_inventory()
            if not available_items or available_items == 0:
                continue
            ore = input("Enter the ore you want to sell: ")
            quantity = int(input(f"Enter the number of units of {ore} you want to sell: "))
            player.sell_from_shop(ore, quantity)
        else:
            print('Invalid input, please try again.')