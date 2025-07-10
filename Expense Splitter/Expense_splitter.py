from datetime import datetime

def view_past_splits():
    print("\n----- Past Expense Splits -----")
    try:
        with open("expenses.txt", "r", encoding="utf-8") as F1:
            data = F1.read()
            if not data.strip():
                print("No past records found.")
            else:
                print(data)
    except FileNotFoundError:
        print("No records found.")
    print("-------------------------------\n")
    input("Press Enter to return to the menu...")

def expense_splitter():
    print("********** Welcome to the Expense Splitter! **********")

    while True:
        print("\nMain Menu:")
        print("1. Split a new expense")
        print("2. View past splits")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            # Get number of people
            while True:
                try:
                    num = int(input("How many people are there? "))
                    if num < 2:
                        print("At least 2 people needed.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number.")

            # Get names
            people = []
            print("Enter names one by one:")
            for i in range(num):
                name = input("> ").strip()
                people.append(name)

            # Get payer
            while True:
                payer = input("Who paid the bill? ").strip()
                if payer not in people:
                    print("Name not found. Try again.")
                else:
                    break

            # Get total amount
            while True:
                try:
                    total = float(input("Total amount? ₹"))
                    if total <= 0:
                        print("Amount must be positive.")
                        continue
                    break
                except ValueError:
                    print("Enter a valid amount.")

            share = round(total / num, 2)
            print(f"\nEach person should pay: ₹{share}\n")

            balances = []
            print("----- Final Balances -----")
            payer_gets = round(total - share, 2)
            print(f"{payer} gets ₹{payer_gets}")
            balances.append(f"{payer} gets ₹{payer_gets}")
            for person in people:
                if person != payer:
                    print(f"{person} owes ₹{share}")
                    balances.append(f"{person} owes ₹{share}")

            # Save to file
            save = input("\nSave this split to file? (Y/N): ").strip().upper()
            if save == 'Y':
                try:
                    with open("expenses.txt", "a", encoding="utf-8") as F1:
                        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
                        F1.write("--- Expense Split Summary ---\n")
                        F1.write(f"Date: {timestamp}\n")
                        F1.write(f"Payer: {payer}, Total: ₹{total}, Each: ₹{share}\n")
                        for b in balances:
                            F1.write(b + "\n")
                        F1.write("-----------------------------\n\n")
                    print("Saved!")
                except Exception as e:
                    print("Error saving file:", e)
            else:
                print("Not saved.")

        elif choice == '2':
            view_past_splits()

        elif choice == '3':
            print("Exited")
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

expense_splitter()
