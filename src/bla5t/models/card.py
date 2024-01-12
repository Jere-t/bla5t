# bla5t/models/card.py
from typing import List

from bla5t.models.ability import Ability


SUIT_LIST = ["x", "♠", "♦", "♥", "♣"]
BACK_CARD_ASCII_ART = [
    "┌─────────┐",
    "│X       X│",
    "│         │",
    "│         │",
    "│    X    │",
    "│         │",
    "│         │",
    "│X       X│",
    "└─────────┘",
]


class Card:
    def __init__(
        self, name: str, ability: Ability, extension: bool = False, image=None
    ):
        self.name = name
        self.ability = ability
        self.extension = extension
        self.image = image

    def card_ascii_art(self) -> List[str]:
        value = self.ability.value
        space = " " if value < 10 else ""
        ascii_art: list[str] = []
        ascii_art.append("┌─────────┐")
        ascii_art.append(
            "│{}{}       │".format(value, space)
        )  # use two {} one for char, one for space or char
        ascii_art.append("│         │")
        ascii_art.append("│         │")
        ascii_art.append("│    {}    │".format(SUIT_LIST[self.ability.sub_value]))
        ascii_art.append("│         │")
        ascii_art.append("│         │")
        ascii_art.append("│       {}{}│".format(space, value))
        ascii_art.append("└─────────┘")

        return ascii_art
