import random

class Character:
    def __init__(self, name, current_room=None):
        self.name = name
        self.current_room = current_room
        self.cards = []

    def move_to_room(self, new_room):
        self.current_room = new_room
        print(f"{self.name} has moved to the {new_room}.")


def assign_characters_to_rooms(characters, mansion_rooms):
    for character in characters:
        character.current_room = random.choice(mansion_rooms)
        print(f"{character.name} starts in the {character.current_room}.")