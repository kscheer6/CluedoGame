import random
from players import Player

class NPC(Player):  
    def __init__(self, name, starting_room):
        super().__init__(name, starting_room) 

    def add_to_notebook(self, entry):
        self.notebook.append(entry)

    def show_notebook(self):
        print(f"\n--- {self.name}'s Notebook ---")
        for entry in self.notebook:
            print(entry)

    def roll_and_set_steps(self, mansion):
        self.remaining_steps = mansion.roll_dice()

    def move(self, target_room, mansion):  
        current_location = self.current_coordinates or mansion.get_room_coordinates(self.current_room)
        reachable, unreachable = mansion.get_reachable_and_unreachable_rooms(current_location, self.remaining_steps)
        unexplored_rooms = [room for room in reachable if room not in [note.get("room") for note in self.notebook]]

        if target_room in reachable:
            super().move(target_room, mansion)
        elif unexplored_rooms:
            target_room = unexplored_rooms[0]
            super().move(target_room, mansion)
        elif reachable:
            target_room = reachable[0]
            super().move(target_room, mansion)
        elif unreachable:
            target_room = min(unreachable, key=lambda x: x[1])[0]
            super().move(target_room, mansion)
        else:
            print(f"{self.name} cannot move this turn.")

    def make_suggestion(self, characters, weapons):
        if self.current_room:
            suggested_character = random.choice([c.name for c in characters if c.name not in self.cards])
            suggested_weapon = random.choice([w.name for w in weapons if w.name not in self.cards])

            print(f"{self.name} suggests: {suggested_character} with the {suggested_weapon} in the {self.current_room}")
            return suggested_character, suggested_weapon, self.current_room

    def make_accusation(self, solution):
        known_murderer = [note["character"] for note in self.notebook if note.get("is_solution") and note["type"] == "character"]
        known_weapon = [note["weapon"] for note in self.notebook if note.get("is_solution") and note["type"] == "weapon"]
        known_room = [note["room"] for note in self.notebook if note.get("is_solution") and note["type"] == "room"]

        if known_murderer and known_weapon and known_room:
            print(f"{self.name} accuses: {known_murderer[0]} with the {known_weapon[0]} in the {known_room[0]}")
            return known_murderer[0] == solution["Murderer"] and known_weapon[0] == solution["Weapon"] and known_room[0] == solution["Room"]
        return None
