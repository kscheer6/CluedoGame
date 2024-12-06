from suggestions import make_suggestion, refute_suggestion

def game_loop(player, characters, weapons, mansion, solution):
    print("\n--- Starting the Game ---")
    print(f"You are currently playing as {player.name}, starting in the {player.current_room}.")

    while True:
        print(f"\nYou are currently in the {player.current_room}.")
        print("Available rooms:", ", ".join(mansion.rooms[player.current_room]))
        
        print("\n--- Your Cards ---")
        print(", ".join(player.cards))
        
        print("\n--- Your Notebook ---")
        player.show_notebook()

        print("\n--- Actions ---")
        print("1. Move to another room")
        print("2. Make a suggestion")
        print("3. View notebook")
        print("4. End the game")
        action = input("Choose an action (1/2/3/4): ")

        if action == "1":
            new_room = input("Enter the room you want to move to: ")
            player.move(new_room, mansion)

        elif action == "2":
            print("\n--- Make a Suggestion ---")
            all_characters = characters + [player]
            suggestion = make_suggestion(player, all_characters, weapons)

            if suggestion:
                refutation = refute_suggestion(player, suggestion, all_characters)
                if refutation:
                    player.add_to_notebook(f"Refutation: {refutation}")
                else:
                    player.add_to_notebook("No refutation for suggestion.")

        elif action == "3":
            player.show_notebook()

        elif action == "4":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Invalid action. Please choose 1, 2, 3, or 4.")
