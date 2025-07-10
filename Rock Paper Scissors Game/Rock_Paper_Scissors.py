import random

def game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    draw_count = 0

    print("**********Welcome to Rock, Paper, Scissors!***********")

    
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("Type 'exit' anytime to quit early.\n")

    current_round = 1
    while current_round <= rounds:
        print(f"Round {current_round} of {rounds}")
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if user_choice == 'exit':
            print("Game exited early by user.")
            break

        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.\n")
            continue

        comp_choice = random.choice(options)
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("It's a draw!")
            draw_count += 1

        elif ((user_choice == "rock" and comp_choice == "scissors") or(user_choice == "paper" and comp_choice == "rock") or(user_choice == "scissors" and comp_choice == "paper")):
            print("You win this round!")
            user_score += 1

        else:
            print("Computer wins this round!")
            comp_score += 1

        print(f"Score — You: {user_score}, Computer: {comp_score}, Draws: {draw_count}\n")
        current_round += 1

    print("Game Over!")
    print(f"Final Score — You: {user_score}, Computer: {comp_score}, Draws: {draw_count}")


    with open("Score.txt", "a") as file:
        file.write(f"Rounds: {current_round - 1}, You: {user_score}, Computer: {comp_score}, Draws: {draw_count}\n")

    print("Your scores have been saved to 'Score.txt'. Thank you for playing!")

game()
