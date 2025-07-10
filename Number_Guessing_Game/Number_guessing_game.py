import random

def get_range():
    print("\n Choose Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 1, 50
        elif choice == '2':
            return 1, 100
        elif choice == '3':
            return 1, 200
        else:
            print("Invalid choice. Please try again.")

def number_guess():
    best_score = None

    while True:
        low, high = get_range()
        num = random.randint(low, high)
        attempts = 0

        print(f"\n I've picked a number between {low} and {high}. Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < low or guess > high:
                    print(f"Please guess a number between {low} and {high}.")
                    continue
                if guess == num:
                    print(f"Correct! You guessed it in {attempts} attempts.")
                    if best_score is None or attempts < best_score:
                        best_score = attempts
                        print("New Best Score!")
                    else:
                        print(f" Best Score: {best_score} attempts")
                    break
                elif abs(guess - num) <= 3:
                    print("Very close!")
                elif guess < num:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")

            except ValueError:
                print("Invalid input! Please enter a number.")

        play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if play_again != 'Y':
            print("Thanks for playing.")
            break

print("*****Welcome to the Number Guessing Game!*****")
number_guess()
