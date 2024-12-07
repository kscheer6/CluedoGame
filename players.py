class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.current_coordinates = None
        self.notebook = []
        self.cards = []
        self.remaining_steps = 0

    def add_to_notebook(self, entry):
        self.notebook.append(entry)
        print(f"Added to notebook: {entry}")

    def show_notebook(self):
        print("\n--- Your Notebook ---")
        for entry in self.notebook:
            print(entry)

    def roll_and_set_steps(self, mansion):
        self.remaining_steps = mansion.roll_dice()

    def move(self, new_room, mansion):
        if self.remaining_steps <= 0:
            print("You need to roll the dice to get steps!")
            return

        start_coordinates = (
            mansion.get_room_coordinates(self.current_room)
            if self.current_room else self.current_coordinates
        )

        if new_room in mansion.rooms:
            end_coordinates = mansion.get_room_coordinates(new_room)
            distance = mansion.calculate_distance(start_coordinates, end_coordinates)

            if mansion.is_valid_move(start_coordinates, end_coordinates, self.remaining_steps):
                self.remaining_steps -= distance
                self.current_room = new_room
                self.current_coordinates = None
                print(f"{self.name} moved to the {new_room}.")
            else:
                print(f"{self.name} doesn't have enough steps to reach {new_room}. Moving toward it.")
                self.move_toward_coordinates(start_coordinates, mansion.get_room_coordinates(new_room))
        else:
            print(f"Invalid move! {new_room} is not a valid room.")


    def move_toward_coordinates(self, start_coordinates, target_coordinates):
        x_diff = target_coordinates[0] - start_coordinates[0]
        y_diff = target_coordinates[1] - start_coordinates[1]

        steps_taken = 0

        if abs(x_diff) > 0:
            x_step = 1 if x_diff > 0 else -1
            while steps_taken < self.remaining_steps and start_coordinates[0] != target_coordinates[0]:
                start_coordinates = (start_coordinates[0] + x_step, start_coordinates[1])
                steps_taken += 1

        if steps_taken < self.remaining_steps and abs(y_diff) > 0:
            y_step = 1 if y_diff > 0 else -1
            while steps_taken < self.remaining_steps and start_coordinates[1] != target_coordinates[1]:
                start_coordinates = (start_coordinates[0], start_coordinates[1] + y_step)
                steps_taken += 1

        self.remaining_steps -= steps_taken
        self.current_coordinates = start_coordinates
        self.current_room = None 
        print(f"{self.name} moved toward coordinates {self.current_coordinates}. Steps remaining: {self.remaining_steps}.")
