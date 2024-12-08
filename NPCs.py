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

    def move(self, new_room, mansion):
        current_location = self.current_coordinates or mansion.get_room_coordinates(self.current_room)
        reachable, unreachable = mansion.get_reachable_and_unreachable_rooms(current_location, self.remaining_steps)

        unexplored_rooms = [room for room in reachable if room not in [note.get("room") for note in self.notebook]]

    # Prioritize unexplored rooms
        target_room = None
        for note in self.notebook:
            if note.get("type") == "suggestion" and not note.get("refuted"):
                target_room = note.get("room")
                break

        if target_room and target_room in reachable:
            super().move(target_room, mansion)
        elif unexplored_rooms:
            target_room = unexplored_rooms[0]
            super().move(target_room, mansion)
        elif reachable:
            target_room = random.choice(reachable)
            super().move(target_room, mansion)
        elif unreachable:
            target_room = min(unreachable, key=lambda x: x[1])[0]
            super().move(target_room, mansion)
        else:
            print(f"{self.name} cannot move this turn.")


    def make_suggestion(self, characters, weapons):
        if self.current_room:
            potential_characters = [c.name for c in characters if c.name not in self.cards]
            potential_weapons = [w.name for w in weapons if w.name not in self.cards]

            suggested_character = random.choice(potential_characters)
            suggested_weapon = random.choice(potential_weapons)

            print(f"{self.name} suggests: {suggested_character} with the {suggested_weapon} in the {self.current_room}")
            return suggested_character, suggested_weapon, self.current_room

    def make_accusation(self, solution):
        potential_murderer = None
        potential_weapon = None
        potential_room = None

        for note in self.notebook:
            if note.get("type") == "refutation" and not note.get("card"):
                if "character" in note:
                    potential_murderer = note["character"]
                elif "weapon" in note:
                    potential_weapon = note["weapon"]
                elif "room" in note:
                    potential_room = note["room"]

        if potential_murderer and potential_weapon and potential_room:
            print(f"{self.name} accuses: {potential_murderer} with the {potential_weapon} in the {potential_room}")
            return (
                potential_murderer == solution["Murderer"]
                and potential_weapon == solution["Weapon"]
                and potential_room == solution["Room"]
            )
        return None

    def update_notebook(self, refutation=None):
        if refutation:
            self.notebook.append(refutation)
        else:
            print(f"{self.name}'s notebook: {self.notebook}")
