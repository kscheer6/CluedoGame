from suggestions import make_suggestion, refute_suggestion
from accusations import make_accusation
import random

def game_loop(player, npcs, characters, weapons, mansion, solution):
    print("\n--- Starting the Game ---")
    print(f"You are currently playing as {player.name}, starting in the {player.current_room}.")

    all_players = [player] + npcs

    while True:
        for current_player in all_players:
            # Player's Turn
            if current_player == player:
                print(f"\n--- {player.name}'s Turn ---")
                print("\n--- Your Cards ---")
                print(", ".join(player.cards))
                player.show_notebook()

                # Roll dice and move
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

                # Check if the player is in a room after moving
                if player.current_room:
                    # Player is in a room, present actions
                    while True:
                        print("\n--- Actions ---")
                        print("1. Make a suggestion")
                        print("2. Make an accusation")
                        print("3. Pass turn")
                        print("4. End the game")
                        action = input("Choose an action (1/2/3/4): ")

                        if action == "1":
                            all_characters = characters + [player]
                            suggestion = make_suggestion(player, all_characters, weapons)

                            if suggestion:
                                refutation = refute_suggestion(player, suggestion, all_characters)
                                if refutation:
                                    player.add_to_notebook(f"Refutation: {refutation}")
                                else:
                                    player.add_to_notebook(f"No refutation for suggestion ({suggestion.character}, {suggestion.weapon}, {suggestion.room}).")
                            break

                        elif action == "2":
                            result = make_accusation(player, solution)
                            if result is True:
                                print(f"{player.name} solved the mystery!")
                                return
                            elif result is False:
                                print("Game over.")
                                return

                        elif action == "3":
                            print("You passed your turn.")
                            break

                        elif action == "4":
                            print("Thanks for playing! Goodbye.")
                            return

                        else:
                            print("Invalid action. Please choose a valid option.")
                else:
                    # Player is not in a room, skip their action phase
                    print(f"{player.name} is not in a room. Skipping action phase.")
                    continue

            # NPC's Turn
            else:
                print(f"\n--- {current_player.name}'s Turn ---")
                # Roll dice and move
                current_player.roll_and_set_steps(mansion)
                current_location = current_player.current_coordinates or mansion.get_room_coordinates(current_player.current_room)
                reachable, unreachable = mansion.get_reachable_and_unreachable_rooms(current_location, current_player.remaining_steps)

                if reachable:
                    target_room = random.choice(reachable)
                    current_player.move(target_room, mansion)
                elif unreachable:
                    target_room = random.choice([room for room, _ in unreachable])
                    current_player.move(target_room, mansion)
                else:
                    print(f"{current_player.name} cannot move this turn.")

                # NPC makes a suggestion if in a room
                if current_player.current_room:
                    suggested_character = random.choice(characters).name
                    suggested_weapon = random.choice(weapons).name
                    print(f"{current_player.name} suggests: {suggested_character} with the {suggested_weapon} in the {current_player.current_room}")
