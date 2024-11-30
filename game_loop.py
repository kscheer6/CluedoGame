from suggestions import make_suggestion

def game_loop(player, characters, weapons, mansion, solution):
    print("\n--- Starting the Game ---")
    print(f"You are currently playing as {player.name}, starting in the {player.current_room}.")

    while True:
        print(f"\nYou are currently in the {player.current_room}.")
        print("Available rooms:", ", ".join(mansion.rooms[player.current_room]))

        print("\n--- Actions ---")
        print("1. Move to another room")
        print("2. Make a suggestion")
        print("3. End the game")
        action = input("Choose an action (1/2/3): ")

        if action == "1":
            new_room = input("Enter the room you want to move to: ")
            player.move(new_room, mansion)

        elif action == "2":
            print("\n--- Make a Suggestion ---")
            all_characters = characters + [player]
            suggestion = make_suggestion(player, all_characters, weapons)

            if suggestion:
                print("\nChecking your suggestion...")
                if (suggestion.character == solution["Murderer"] and
                        suggestion.weapon == solution["Weapon"] and
                        suggestion.room == solution["Room"]):
                    print("\nCongratulations! You solved the mystery!")
                    print(f"The murderer was {solution['Murderer']} with the {solution['Weapon']} in the {solution['Room']}.")
                    break
                else:
                    print("\nYour suggestion is incorrect. Keep investigating!")

        elif action == "3":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Invalid action. Please choose 1, 2, or 3.")
