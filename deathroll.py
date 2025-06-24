import random

def deathroll_game():
    print("Welcome to Deathroll!")
    max_roll = int(input("Enter the starting maximum number for the roll: "))
    player_turn = 1

    while True:
        print(f"\nPlayer {player_turn}'s turn.")
        input("Press Enter to roll the dice...")

        roll_result = random.randint(1, max_roll)
        print(f"You rolled a {roll_result}!")

        if roll_result == 1:
            print(f"Player {player_turn} rolled a 1 and loses!")
            break
        else:
            max_roll = roll_result
            print(f"The new maximum roll is {max_roll}.")
            player_turn = 2 if player_turn == 1 else 1 # Switch turns

if __name__ == "__main__":
    deathroll_game()