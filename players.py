class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.notebook = []
        self.cards = []

    def move(self, new_room, mansion):
        if new_room in mansion.rooms[self.current_room]:
            self.current_room = new_room
            print(f"{self.name} moved to the {new_room}.")
        else:
            print(f"Invalid move! {new_room} is not connected to {self.current_room}.")

    def add_to_notebook(self, entry):
        self.notebook.append(entry)
        print(f"Added to notebook: {entry}")

    def show_notebook(self):
        print("\n--- Your Notebook ---")
        for entry in self.notebook:
            print(entry)
