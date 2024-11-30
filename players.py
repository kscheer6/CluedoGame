class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def move(self, new_room, mansion):
        if new_room in mansion.rooms[self.current_room]:
            self.current_room = new_room
            print(f"{self.name} moved to the {new_room}.")
        else:
            print(f"Invalid move! {new_room} is not connected to {self.current_room}.")