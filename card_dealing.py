import random
from itertools import chain

def deal_cards(characters, weapons, mansion_rooms, players, solution):
    """
    Distributes cards among players, excluding the solution cards.
    :param characters: List of Character objects.
    :param weapons: List of Weapon objects.
    :param mansion_rooms: Dictionary of mansion rooms.
    :param players: List of Player objects.
    :param solution: Dictionary containing the solution cards.
    :return: None
    """
    deck = list(chain(
        [character.name for character in characters],
        [weapon.name for weapon in weapons],
        mansion_rooms
    ))

    deck = [card for card in deck if card not in solution.values()]

    random.shuffle(deck)

    for i, card in enumerate(deck):
        players[i % len(players)].cards.append(card)

    for player in players:
        print(f"{player.name} has cards: {', '.join(player.cards)}")
