import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and versatile programming language.",
    "Typing fast is a useful skill in today's digital world.",
    "Practice makes perfect when learning to code.",
    "Never stop exploring new ideas and possibilities."
]

def typing_test():
    print("********** Typing Speed Test **********")

    while True:
        sentence = random.choice(sentences)
        print("\nType the following sentence:\n")
        print(sentence)
        input("\nPress Enter when you're ready...")

        start_time = time.time()
        typed = input("\nStart typing: ")
        end_time = time.time()

        time_taken = round(end_time - start_time, 2)

        if not typed.strip():
            print("You didn't type anything. Try again.\n")
            continue

        if time_taken < 1:
            print("You typed too fast. Try again.\n")
            continue

        total_words = len(sentence.split())
        wpm = round((total_words / time_taken) * 60, 2)

        mistakes = 0
        for i in range(min(len(sentence), len(typed))):
            if sentence[i] != typed[i]:
                mistakes += 1
        mistakes += abs(len(sentence) - len(typed))

        accuracy = round(((len(sentence) - mistakes) / len(sentence)) * 100, 2)

        print("\n----- Results -----")
        print(f"Time Taken: {time_taken} seconds")
        print(f"WPM: {wpm}")
        print(f"Accuracy: {accuracy}%")
        print(f"Mistakes: {mistakes}")

        again = input("\nPlay again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thanks for playing!")
            break

typing_test()
