import random
from typing import List

from bla5t.models.card import Card


class Croupier:
    @staticmethod
    def shuffle_deck(deck: List[Card]):
        """
        Shuffle the given deck of cards using a random process.

        :param deck: The list of cards representing the deck to be shuffled.

        The function shuffles the deck five times to ensure a thorough mixing.
        """
        for _ in range(5):
            random.shuffle(deck)
