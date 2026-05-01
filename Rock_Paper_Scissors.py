import random
from datetime import datetime

# Take player name
player_name = input("Enter your name: ")

# Score variables
user_score = 0
computer_score = 0

# Dictionaries
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

# Main game loop
while True:

    # Computer choice
    computer = random.choice([-1, 0, 1])

    # User input
    youstr = input("\nEnter your choice (r = Rock, p = Paper, s = Scissors): ").lower()

    # Input validation
    if youstr not in youDict:
        print("Invalid input! Please enter r, p, or s.")
        continue

    # Convert user input
    you = youDict[youstr]

    # Show choices
    print(f"\n{player_name} chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    # Game logic
    if computer == you:
        print("It's a draw!")

    else:
        if (computer - you) == -1 or (computer - you) == 2:
            print("You lose!")
            computer_score += 1

        else:
            print("You win!")
            user_score += 1

    # Display score
    print("\n----- SCORE BOARD -----")
    print(f"{player_name}: {user_score}")
    print(f"Computer: {computer_score}")

    # Replay option
    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":

        # Final result
        print("\n----- FINAL RESULT -----")
        print(f"{player_name}: {user_score}")
        print(f"Computer: {computer_score}")

        if user_score > computer_score:
            result = "Won"

        elif computer_score > user_score:
            result = "Lost"

        else:
            result = "Draw"

        print(f"Match Result: {result}")

        # Current date and time
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save score in file
        with open("stone_paper_scissors_game_scores.txt", "a") as file:
            file.write(
                f"Date: {current_date} | "
                f"Player: {player_name} | "
                f"Player Score: {user_score} | "
                f"Computer Score: {computer_score} | "
                f"Result: {result}\n"
            )

        print("\nScore saved successfully in 'rock_paper_scisors_game_scores.txt'")

        print("\nThanks for playing!")
        break
