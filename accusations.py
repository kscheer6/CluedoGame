def make_accusation(player, solution):
    print("\n--- Make an Accusation ---")
    print("If your accusation is correct, you win. If incorrect, you lose.")
    confirm = input("Are you sure you want to make an accusation? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Accusation canceled.")
        return None

    character = input("Who do you accuse as the murderer? ").strip()
    weapon = input("What weapon do you accuse was used? ").strip()
    room = input("Which room do you accuse the murder happened in? ").strip()

    if character == solution["Murderer"] and weapon == solution["Weapon"] and room == solution["Room"]:
        print("\nCongratulations! Your accusation is correct. You win!")
        print(f"The solution was: {solution['Murderer']} with the {solution['Weapon']} in the {solution['Room']}.")
        return True
    else:
        print("\nYour accusation is incorrect.")
        print(f"You lose! The solution was: {solution['Murderer']} with the {solution['Weapon']} in the {solution['Room']}.")
        return False
