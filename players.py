class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.notebook = []  

    def add_to_notebook(self, entry):
        self.notebook.append(entry)
        print(f"Added to notebook: {entry}")

    def show_notebook(self):
        print(f"\n--- {self.name}'s Notebook ---")
        for entry in self.notebook:
            print(entry)
