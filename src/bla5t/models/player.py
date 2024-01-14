import copy
from typing import List

from bla5t.models.card import BACK_CARD_ASCII_ART, Card


class Player:
    def __init__(self, name: str, front_cards: List[Card] = None, hand: Card = None):
        self.name = name
        self.front_cards = front_cards
        self.hand = hand
        self.score = 0

    @classmethod
    def create_new_players(cls):
        players_list: List[cls] = []
        for i in range(5):
            name = input("Enter player name or press enter to finish: ")
            if len(name) > 0:
                players_list.append(cls(name))
            else:
                if len(players_list) < 2:
                    print("You need to add at least 2 players to play this game.")
                else:
                    break

        return players_list

    def add_front_cards(self, deck: List[Card]):
        self.front_cards = []
        for _ in range(4):
            self.front_cards.append(deck.pop(0))

    def show_front_cards(self):
        front_cards_str: List[str] = []

        for index, card in enumerate(self.front_cards, 1):
            back_card = copy.copy(BACK_CARD_ASCII_ART)
            back_card[8] = f"{back_card[8]} {index}"
            front_cards_str.extend(back_card)
            front_cards_str.append("")

        for row in front_cards_str:
            print(row)
