import random

class Mansion:
    def __init__(self):
        # Define the grid layout of the mansion
        self.grid = {
            "Kitchen": (0, 0),
            "Library": (0, 4),
            "Lounge": (0, 8),
            "Hall": (3, 0),
            "Billiard Room": (6, 0),
            "Conservatory": (8, 0),
            "Ballroom": (8, 4),
            "Study": (8, 8),
            "Dining Room": (4, 8),
        }
        self.rooms = list(self.grid.keys())

    def roll_dice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"\nRolled a {die1} and a {die2}. Total steps: {total}")
        return total

    def calculate_distance(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def is_valid_move(self, start, end, steps):
        distance = self.calculate_distance(start, end)
        return distance <= steps

    def get_reachable_and_unreachable_rooms(self, current_coordinates, steps):
        reachable = []
        unreachable = []

        for room, coordinates in self.grid.items():
            distance = self.calculate_distance(current_coordinates, coordinates)
            if distance <= steps:
                reachable.append(room)
            else:
                remaining_distance = abs(distance - steps)
                unreachable.append((room, remaining_distance))

        return reachable, unreachable
    
    def get_room_coordinates(self, room):
        return self.grid.get(room)