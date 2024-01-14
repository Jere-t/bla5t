from typing import List

from bla5t.models.card import Card
from bla5t.models.player import Player


class Game:
    def __init__(self, players: List[Player], deck: List[Card]):
        self.deck = deck
        self.players = players
        self.bla5t: Player = None
        self.discard: List[Card] = []

    def start_game(self):
        self.discard = []
        while self.bla5t is None:
            print("Let's start the game...")
            for player in self.players:
                print(f"{player.name}, it's your turn.")

                bla5t_call = "?"
                while bla5t_call != "yes" or bla5t_call != "no" or bla5t_call != "":
                    bla5t_call = input("Do you want to call Bla5t yes/no [no]")
                if bla5t_call == "yes":
                    self.bla5t = player
            self.do_bla5t_turn()

    def do_bla5t_turn(self):
        # ToDo: define next player to play, and next one...
        pass
