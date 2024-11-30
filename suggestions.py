class Suggestion:
    def __init__(self, character, weapon, room):
        self.character = character
        self.weapon = weapon
        self.room = room

    def __str__(self):
        return f"Suggestion: {self.character} with the {self.weapon} in the {self.room}"

def make_suggestion(player, characters, weapons):
    if player.current_room is None:
        print("You must be in a room to make a suggestion!")
        return None

    print("\n--- Make a Suggestion ---")
    print(f"You're in the {player.current_room}.")
    character_names = [character.name for character in characters]
    weapon_names = [weapon.name for weapon in weapons]

    print(f"Characters: {', '.join(character_names)}")
    suggested_character = input("Choose a character: ")

    print(f"Weapons: {', '.join(weapon_names)}")
    suggested_weapon = input("Choose a weapon: ")

    suggestion = Suggestion(suggested_character, suggested_weapon, player.current_room)
    print("\nYour suggestion:", suggestion)
    return suggestion