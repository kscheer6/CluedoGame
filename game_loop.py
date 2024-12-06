from suggestions import make_suggestion, refute_suggestion
from accusations import make_accusation

def game_loop(player, characters, weapons, mansion, solution):
    print("\n--- Starting the Game ---")
    print(f"You are currently playing as {player.name}, starting in the {player.current_room}.")

    while True:
        if player.current_room:
            print(f"\nYou are currently in the {player.current_room}.")
        else:
            nearest_room, distance = min(
                [(room, mansion.calculate_distance(player.current_coordinates, mansion.get_room_coordinates(room)))
                 for room in mansion.rooms],
                key=lambda x: x[1]
            )
            print(f"\nYou are not currently in a room and are {distance} steps from the nearest room, the {nearest_room}.")
        
        #print(f"Available steps: {player.remaining_steps}")

        print("\n--- Your Cards ---")
        print(", ".join(player.cards))
        
        player.show_notebook()

        print("\n--- Actions ---")
        print("1. Roll dice and move")
        print("2. Make a suggestion")
        print("3. Make an accusation")
        print("4. View notebook")
        print("5. End the game")
        action = input("Choose an action (1/2/3/4/5): ")

        if action == "1":
            player.roll_and_set_steps(mansion)
            current_location = player.current_coordinates or mansion.get_room_coordinates(player.current_room)
            reachable, unreachable = mansion.get_reachable_and_unreachable_rooms(current_location, player.remaining_steps)

            print("\nYou can reach the following rooms:")
            print(", ".join(reachable))

            print("\nOr you can move towards the following rooms (with updated distance from you):")
            for room, remaining_distance in unreachable:
                print(f"{room}: {remaining_distance} steps away")

            while True:
                selected_room = input("\nEnter the room you want to move to(wards): ").strip().title()
                if selected_room in reachable:
                    player.move(selected_room, mansion)
                    break
                elif selected_room in [room for room, _ in unreachable]:
                    player.move(selected_room, mansion)
                    break
                else:
                    print("Invalid choice! Please select a valid room or direction.")


        elif action == "2":
            all_characters = characters + [player]
            suggestion = make_suggestion(player, all_characters, weapons)

            if suggestion:
                refutation = refute_suggestion(player, suggestion, all_characters)
                if refutation:
                    player.add_to_notebook(f"Refutation: {refutation}")
                else:
                    player.add_to_notebook(f"No refutation for suggestion ({suggestion.character}, {suggestion.weapon}, {suggestion.room}).")

        elif action == "3":
            result = make_accusation(player, solution)
            if result is True:
                break
            elif result is False:
                print("Game over.")
                break
                        
        elif action == "4":
            player.show_notebook()

        elif action == "5":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Invalid action. Please choose a valid option.")
