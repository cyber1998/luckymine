import pandas as pd
from player import Player
from utils import object_name

class Game(object):

    def __init__(self):
        self.player = None

    def create_player(self, name=None):
        player = Player(name=name)
        self.player = player
    
    def get_player(self):
        return self.player

    def get_assets(self):
        df = pd.DataFrame(list(self.player.get_assets()))
        df.columns = ["Assets"]
        df.applymap(lambda x: object_name(x))
        return df

    def get_player_balance(self):
        return self.player.get_account_balance()
    