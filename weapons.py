import random

class Weapon:
    def __init__(self, name, current_room=None):
        self.name = name
        self.current_room = current_room

def assign_weapons_to_rooms(weapons, mansion_rooms):
    for weapon in weapons:
        weapon.current_room = random.choice(mansion_rooms)
        print(f"The {weapon.name} is placed in the {weapon.current_room}.")