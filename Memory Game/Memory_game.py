import random
import time
import os

def memory_trainer():
    print("********** Memory Trainer Game **********")

    while True:
        sequence = [str(random.randint(10, 99)) for _ in range(5)]
        print("\nMemorize this sequence:\n")
        print(" ".join(sequence))
        time.sleep(5)

        os.system('cls' if os.name == 'nt' else 'clear')

        
        user_input = input("Enter the sequence (space-separated): ").strip().split()

        
        if user_input == sequence:
            print("Correct! Great memory!")
        else:
            print("Oops! That's not quite right.")
            print("Correct sequence was:", " ".join(sequence))

        again = input("\nPlay again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thanks for training your brain, See you soon!")
            break

memory_trainer()
