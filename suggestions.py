import random

class Suggestion:
    def __init__(self, player_name, character, weapon, room):
        self.player_name = player_name
        self.character = character
        self.weapon = weapon
        self.room = room

    def __str__(self):
        return f"Suggestion by {self.player_name}: {self.character} with the {self.weapon} in the {self.room}"


def make_suggestion(player, characters, weapons):
    if player.current_room is None:
        print("You must be in a room to make a suggestion!")
        return None

    print("\n--- Make a Suggestion ---")
    print(f"You're in the {player.current_room}.")
    character_names = [character.name.lower() for character in characters]
    weapon_names = [weapon.name.lower() for weapon in weapons]

    while True:
        print(f"Characters: {', '.join([name.title() for name in character_names])}")
        suggested_character = input("Choose a character: ").strip().lower()
        if suggested_character in character_names:
            suggested_character = [character.name for character in characters if character.name.lower() == suggested_character][0]
            break
        else:
            print("Invalid character. Please choose a valid character from the list.")

    while True:
        print(f"Weapons: {', '.join([name.title() for name in weapon_names])}")
        suggested_weapon = input("Choose a weapon: ").strip().lower()
        if suggested_weapon in weapon_names:
            suggested_weapon = [weapon.name for weapon in weapons if weapon.name.lower() == suggested_weapon][0]
            break
        else:
            print("Invalid weapon. Please choose a valid weapon from the list.")

    suggestion = Suggestion(player.name, suggested_character, suggested_weapon, player.current_room)
    print("\nYour suggestion:", suggestion)
    return suggestion


def refute_suggestion(suggester, suggestion, all_players):
    print(f"\n--- Refuting Suggestion: {suggestion} ---")

    for other_player in all_players:
        if other_player.name == suggester.name:
            continue

        matching_cards = []
        if suggestion.character in other_player.cards:
            matching_cards.append(suggestion.character)
        if suggestion.weapon in other_player.cards:
            matching_cards.append(suggestion.weapon)
        if suggestion.room in other_player.cards:
            matching_cards.append(suggestion.room)

        if matching_cards:
            revealed_card = random.choice(matching_cards)
            print(f"{other_player.name} can refute. They reveal: {revealed_card}")
            return revealed_card

    print("No one can refute this suggestion.")
    return None
