import random
from players import Player

class NPC(Player):
    def __init__(self, name, starting_room):
        super().__init__(name, starting_room)

    def take_turn(self, mansion, characters, weapons):
        """
        Execute the NPC's turn:
        1. Roll dice and move randomly.
        2. Make a suggestion if in a room.
        """
        print(f"\n--- {self.name}'s Turn ---")
        self.roll_and_set_steps(mansion)

        current_location = self.current_coordinates or mansion.get_room_coordinates(self.current_room)
        reachable, unreachable = mansion.get_reachable_and_unreachable_rooms(current_location, self.remaining_steps)

        if reachable:
            target_room = random.choice(reachable)
            self.move(target_room, mansion)
        elif unreachable:
            target_room = random.choice([room for room, _ in unreachable])
            self.move(target_room, mansion)
        else:
            print(f"{self.name} cannot move this turn.")

        if self.current_room:
            self.make_suggestion(characters, weapons)

    def make_suggestion(self, characters, weapons):
        suggested_character = random.choice(characters).name
        suggested_weapon = random.choice(weapons).name
        print(f"{self.name} suggests: {suggested_character} with the {suggested_weapon} in the {self.current_room}")
