import random
from mansion import Mansion
from characters import Character, assign_characters_to_rooms
from players import Player
from NPCs import NPC
from weapons import Weapon, assign_weapons_to_rooms
from solution import select_solution
from game_loop import game_loop
from card_dealing import deal_cards 

mansion = Mansion()
characters = [
    Character("Miss Scarlett"),
    Character("Colonel Mustard"),
    Character("Mrs. White"),
    Character("Mr. Green"),
    Character("Mrs. Peacock"),
    Character("Professor Plum")
]
assign_characters_to_rooms(characters, mansion.rooms)

player_character = random.choice(characters)
characters.remove(player_character)
player = Player(player_character.name, player_character.current_room)
npcs = [NPC(character.name, character.current_room) for character in characters]  

print(f"You are playing as {player.name}, starting in the {player.current_room}.\n")

weapons = [Weapon(name) for name in ["Candlestick", "Revolver", "Rope", "Lead Pipe", "Knife", "Wrench"]]
assign_weapons_to_rooms(weapons, mansion.rooms)

all_players = [player] + characters

solution = select_solution(all_players, weapons, mansion.rooms)

deal_cards(all_players, weapons, mansion.rooms, all_players, solution)

print("\nWelcome to the Cluedo Game!")
print("Your objective is to solve the mystery of the murder.")
print("Find out who the murderer is, the weapon used, and the room where it happened.\n")
print("Solution has been selected! (For debugging purposes)")
print(f"Murderer: {solution['Murderer']}")
print(f"Weapon: {solution['Weapon']}")
print(f"Room: {solution['Room']}")

game_loop(player, npcs, characters, weapons, mansion, solution)
