def make_accusation(player, solution):
    if player.current_room is None:
        print("You must be in a room to make an accusation!")
        return None

    while True:
        print("\n--- Make an Accusation ---")
        print("If your accusation is correct, you win. If incorrect, the game is over and you lose.")
        confirm = input("Are you sure you want to make an accusation? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Accusation canceled.")
            return None

        character = input("Who do you accuse as the murderer? ").strip()
        weapon = input("What weapon do you accuse was used? ").strip()
        room = player.current_room

        # Confirm the accusation details before proceeding
        print(f"\nYou are accusing: {character} with the {weapon} in the {room}.")
        final_confirm = input("Are you sure you want to proceed with this accusation? (yes/no): ").strip().lower()

        if final_confirm == "yes":
            # Check if the accusation is correct
            if character == solution["Murderer"] and weapon == solution["Weapon"] and room == solution["Room"]:
                print("\nCongratulations! Your accusation is correct. You win!")
                print(f"The solution was: {solution['Murderer']} with the {solution['Weapon']} in the {solution['Room']}.")
                return True
            else:
                print("\nYour accusation is incorrect.")
                print(f"You lose! The solution was: {solution['Murderer']} with the {solution['Weapon']} in the {solution['Room']}.")
                return False
        else:
            print("\nLet's start the accusation process again.")
