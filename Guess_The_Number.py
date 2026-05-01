import random
from datetime import datetime

print("===== NUMBER GUESSING GAME =====")

# Take player name
player_name = input("Enter your name: ")

# Best score tracking
best_score = 0

# Replay system
while True:

    # Random number
    number = random.randint(1, 100)

    # Attempt counter
    guesses = 0

    print(f"\nWelcome {player_name}!")
    print("I have selected a number between 1 and 100.")

    # Game loop
    while True:

        # Input validation
        try:
            user_guess = int(input("Guess the number: "))

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Increase attempts
        guesses += 1

        # Hint system
        if user_guess > number:
            print("Lower number please!")

        elif user_guess < number:
            print("Higher number please!")

        else:
            print(f"\nCorrect! You guessed the number {number} correctly.")

            # Score calculation
            current_score = 100 - guesses

            # Prevent negative score
            if current_score < 0:
                current_score = 0

            print(f"You guessed it in {guesses} attempts.")
            print(f"Your Score: {current_score}")

            # Best score tracking
            if current_score > best_score:
                best_score = current_score
                print("New High Score!")

            print(f"Best Score: {best_score}")

            # Current date and time
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Save score in file
            with open("guess_game_scores.txt", "a") as file:
                file.write(
                    f"Date: {current_date} | "
                    f"Player Name: {player_name} | "
                    f"Attempts: {guesses} | "
                    f"Score: {current_score} | "
                    f"Best Score: {best_score}\n"
                )

            print("Score saved successfully!")

            break

    # Replay system
    while True:

        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again == "y":
            break

        elif play_again == "n":
            print("\nThanks for playing!")
            exit()

        else:
            print("Invalid input! Please enter y or n.")
