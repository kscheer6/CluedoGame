import random

def select_solution(characters, weapons, mansion_rooms):
    murderer = random.choice(characters).name
    weapon = random.choice(weapons).name
    room = random.choice(list(mansion_rooms.keys()))
    return {"Murderer": murderer, "Weapon": weapon, "Room": room}