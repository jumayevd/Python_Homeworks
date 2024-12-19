import random

def number_guessing_game():
    response_list = ["YES", "yes", "Y", "y", "ok"]

    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print("Welcome to the number guessing game!")
        while attempts < 10:
            try:
                guess = int(input("Enter your guess between 1 and 100: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            attempts += 1

            if guess > number_to_guess:
                print("Too high!")
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        else:
            print(f"Sorry, you've run out of attempts! The correct number was {number_to_guess}.")

        replay = input("Do you want to play again? (YES/yes/Y/y/ok): ").strip()
        if replay not in response_list:
            print("Thanks for playing! Goodbye!")
            break

number_guessing_game()

