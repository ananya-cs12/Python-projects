import random



def load_quotes():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as F1:
            return [line.strip() for line in F1 if line.strip()]
    except FileNotFoundError:
        return []

def save_quote(quote):
    with open("quotes.txt", "a", encoding="utf-8") as F1:
        F1.write(quote + "\n")

def show_menu():
    print("\nMenu:")
    print("1. Show me a random quote")
    print("2. Add a new quote")
    print("3. View all quotes")
    print("4. Exit")

def quote_generator():
    print("********** Random Quote Generator **********")
    quotes = load_quotes()

    while True:
        show_menu()
        choice = input("Choose an option (1–4): ").strip()

        if choice == '1':
            if quotes:
                print("\nQuote:\n" + random.choice(quotes))
            else:
                print("No quotes available. Please add one first!")

        elif choice == '2':
            new_quote = input("Enter your quote: ").strip()
            if new_quote:
                quotes.append(new_quote)
                save_quote(new_quote)
                print("Quote added and saved!")

        elif choice == '3':
            if quotes:
                print("\nAll Quotes:")
                for idx, q in enumerate(quotes, 1):
                    print(f"{idx}. {q}")
            else:
                print("No quotes to display.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

quote_generator()
