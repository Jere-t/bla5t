from typing import List

from bla5t.models.ability import Ability
from bla5t.models.card import Card


# A hero played for his power can’t be recovered in the discard pile by the next player.
ABILITY_ZERO_ONE = Ability(
    value=0,
    sub_value=1,
    text_en="Swap 1 to 4 of your current cards with one or more opponents",
    text_fr="Echangez 1 à 4 de vos cartes actuelles avec un ou plusieurs adversaires",
)
ABILITY_ZERO_TWO = Ability(
    value=0,
    sub_value=2,
    text_en="If you have this card at the end of the round, you can’t take more than 10 points (except for penalty "
    "points)",
    text_fr="Si vous possédez cette carte à la fin de la manche, vous ne pouvez pas subir plus de 10 points (excepté "
    "points de pénalité)",
)
ABILITY_ZERO_THREE = Ability(
    value=0,
    sub_value=3,
    text_en="Check all your cards and play an extra turn",
    text_fr="Regardez toutes vos cartes et rejouez un tour",
)
ABILITY_ZERO_FOUR = Ability(
    value=0,
    sub_value=4,
    text_en="If an opponent touches this card you can reveal it, it is locked (it remains face up and can’t be "
    "exchanged anymore)",
    text_fr="Si un joueur adverse touche cette carte vous pouvez la révéler, elle est alors verrouillée (elle reste "
    "face visible et ne peut plus être échangée)",
)
ABILITY_ONE = Ability(value=1, sub_value=0, text_en="", text_fr="")
ABILITY_TWO = Ability(value=2, sub_value=0, text_en="", text_fr="")
ABILITY_THREE = Ability(value=3, sub_value=0, text_en="", text_fr="")
ABILITY_FOUR = Ability(value=4, sub_value=0, text_en="", text_fr="")
ABILITY_FIVE = Ability(value=5, sub_value=0, text_en="", text_fr="")
ABILITY_SIX_ONE = Ability(
    value=6,
    sub_value=1,
    text_en="Swap a card between two of your opponents",
    text_fr="Echangez une carte entre deux de vos adversaires",
)
ABILITY_SIX_TWO = Ability(
    value=6,
    sub_value=2,
    text_en="Shuffle two of your cards (or pretend) out of sight and put them back in front of you",
    text_fr="Mélangez deux de vos cartes (ou faites semblant) à l’abri des regards et replacez-les devant vous",
)
ABILITY_SEVEN = Ability(
    value=7,
    sub_value=0,
    text_en="Look at one of your cards",
    text_fr="Regardez une de vos cartes",
)
ABILITY_EIGHT = Ability(
    value=8,
    sub_value=0,
    text_en="Look at an opponent’s card",
    text_fr="Regardez une carte adverse",
)
ABILITY_NINE = Ability(
    value=9,
    sub_value=0,
    text_en="Look at one of your cards then the first of the draw pile",
    text_fr="Regardez une de vos cartes ainsi que la première de la pioche",
)
ABILITY_TEN = Ability(
    value=10,
    sub_value=0,
    text_en="Look at an opponent’s card then the first of the draw pile",
    text_fr="Regardez une carte adverse ainsi que la première de la pioche",
)
ABILITY_ELEVEN = Ability(
    value=11,
    sub_value=0,
    text_en="Swap one of your cards with an opponent’s card without looking at them",
    text_fr="Echangez une de vos cartes avec celle d’une adversaire sans les regarder",
)
ABILITY_TWELVE = Ability(
    value=12,
    sub_value=0,
    text_en="Look at an opponent card; if you want to you can exchange it",
    text_fr="Regardez une carte adverse, vous pouvez l’échanger avec l’une des vôtres",
)
ABILITY_FOURTEEN_ONE = Ability(
    value=14,
    sub_value=1,
    text_en="Combo 2/3/4: Your opponents start the next round without looking at their cards",
    text_fr="Combo 2/3/4: Vos adversaires commencent la manche suivante sans regarder leurs cartes",
)
ABILITY_FOURTEEN_TWO = Ability(
    value=14,
    sub_value=2,
    text_en="Combo 2/3/4: Your opponents start the next round with one extra card",
    text_fr="Combo 2/3/4: Vos adversaires commencent la manche suivante avec une carte de plus",
)

DECK_OF_CARDS: List[Card] = [
    Card(name="Jayce", ability=ABILITY_ZERO_ONE),
    Card(name="Herman", ability=ABILITY_ZERO_TWO),
    Card(name="Calypso", ability=ABILITY_ZERO_THREE),
    Card(name="Helmut", ability=ABILITY_ZERO_FOUR),
    Card(name="Gordon", ability=ABILITY_FOURTEEN_ONE),
    Card(name="Futura", ability=ABILITY_FOURTEEN_TWO),
]

for _ in range(2):
    DECK_OF_CARDS.append(Card(name="Diana", ability=ABILITY_SIX_ONE))
    DECK_OF_CARDS.append(Card(name="Brandon", ability=ABILITY_SIX_TWO))

for _ in range(4):
    DECK_OF_CARDS.append(Card(name="E-zmo", ability=ABILITY_ONE))
    DECK_OF_CARDS.append(Card(name="Bob", ability=ABILITY_TWO))
    DECK_OF_CARDS.append(
        Card(
            name="Ultimate radioactive bloodthirsty giant mutated killer fruit flies of doom",
            ability=ABILITY_THREE,
        )
    )
    DECK_OF_CARDS.append(Card(name="Sharkonaut", ability=ABILITY_FOUR))
    DECK_OF_CARDS.append(
        Card(name="The nowifi's from outerspace", ability=ABILITY_FIVE)
    )
    DECK_OF_CARDS.append(Card(name="Creature of the Pool", ability=ABILITY_SEVEN))
    DECK_OF_CARDS.append(Card(name="The nutzians", ability=ABILITY_EIGHT))
    DECK_OF_CARDS.append(Card(name="Party Alien", ability=ABILITY_NINE))
    DECK_OF_CARDS.append(Card(name="Carnivorous Brussels Sprout", ability=ABILITY_TEN))
    DECK_OF_CARDS.append(Card(name="Yetirminator", ability=ABILITY_ELEVEN))
    DECK_OF_CARDS.append(Card(name="Propzilla", ability=ABILITY_TWELVE))
