import random
from itertools import chain

def deal_cards(characters, weapons, mansion_rooms, players):
    """
    Distributes cards among players after excluding the solution.
    :param characters: List of Character objects.
    :param weapons: List of Weapon objects.
    :param mansion_rooms: Dictionary of mansion rooms.
    :param players: List of Player objects.
    :return: None
    """
    deck = list(chain(
        [character.name for character in characters],
        [weapon.name for weapon in weapons],
        list(mansion_rooms.keys())
    ))

    random.shuffle(deck)

    for i, card in enumerate(deck):
        players[i % len(players)].cards.append(card)

    for player in players:
        print(f"{player.name} has cards: {', '.join(player.cards)}")
