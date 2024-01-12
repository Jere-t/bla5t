"""
Package interface.

This is the main package interface.
"""
from bla5t import cli_int1
from bla5t.configs.card_deck import DECK_OF_CARDS
from bla5t.models.card import Card
from bla5t.services.croupier import Croupier


def main():
    print(f"There are {len(DECK_OF_CARDS)} cards in the deck.")
    deck = DECK_OF_CARDS
    first_card: Card = deck[0]
    card_ascii = first_card.card_ascii_art()
    for row in card_ascii:
        print(row)
    Croupier.shuffle_deck(deck)
    first_card: Card = deck[0]
    card_ascii = first_card.card_ascii_art()
    for row in card_ascii:
        print(row)
    cli_int1.main()


if __name__ == "__main__":
    main()
