from mansion import Mansion

mansion = Mansion()
total = mansion.roll_dice()
assert 2 <= total <= 12, f"Dice roll out of range: {total}"


assert mansion.calculate_distance((0, 0), (3, 4)) == 7
assert mansion.calculate_distance((3, 0), (3, 4)) == 4


assert mansion.is_valid_move((0, 0), (0, 4), 5) == True
assert mansion.is_valid_move((0, 0), (8, 8), 10) == False
