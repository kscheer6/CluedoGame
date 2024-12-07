def make_accusation(player, solution):
    if player.current_room is None:
        print("You must be in a room to make an accusation!")
        return None

    # List of all valid characters and weapons
    characters = ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]
    weapons = ["Candlestick", "Revolver", "Rope", "Lead Pipe", "Knife", "Wrench"]

    while True:
        print("\n--- Make an Accusation ---")
        print("If your accusation is correct, you win. If incorrect, the game is over and you lose.")
        confirm = input("Are you sure you want to make an accusation? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Accusation canceled.")
            return None

        # Validate character input
        while True:
            print(f"Characters: {', '.join(characters)}")
            character = input("Who do you accuse as the murderer? ").strip().title()
            if character in characters:
                break
            else:
                print("Invalid character. Please choose a valid character from the list.")

        # Validate weapon input
        while True:
            print(f"Weapons: {', '.join(weapons)}")
            weapon = input("What weapon do you accuse was used? ").strip().title()
            if weapon in weapons:
                break
            else:
                print("Invalid weapon. Please choose a valid weapon from the list.")

        # Room is automatically the player's current room
        room = player.current_room

        print(f"\nYou are accusing: {character} with the {weapon} in the {room}.")
        final_confirm = input("Are you sure you want to proceed with this accusation? (yes/no): ").strip().lower()

        if final_confirm == "yes":
            # Check accusation against the solution
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
