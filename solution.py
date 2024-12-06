import random

def select_solution(characters, weapons, mansion_rooms):
    murderer = random.choice(characters).name
    weapon = random.choice(weapons).name
    room = random.choice(mansion_rooms)
    return {"Murderer": murderer, "Weapon": weapon, "Room": room}