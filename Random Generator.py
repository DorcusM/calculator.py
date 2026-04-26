 import random

def play_game():
    # Bonus: start with range 1–100, increase each round
    lower = 1
    upper = 100
    round_number = 1

    while True:
        print(f"\nRound {round_number}: Guess the number between {lower} and {upper}")
        secret_number = random.randint(lower, upper)
        attempts = 0
        max_attempts = 7

        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts+1}/{max_attempts}: Enter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue  # don’t count invalid input as an attempt

            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! 🎉 You guessed it in {attempts} attempts.")
                break
        else:
            # Only runs if loop ends without a break
            print(f"Game Over! The correct number was {secret_number}.")

        # Ask if player wants to continue
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        else:
            # Bonus: make next round harder by expanding the range
            upper += 50
            round_number += 1

# Run the game
if __name__ == "__main__":
    play_game()
