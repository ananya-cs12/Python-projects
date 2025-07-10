def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose option (1/2): ")

    try:
        length = float(input("Enter value: "))
        if choice == '1':
            print(f"{length} km = {round(length * 0.621371, 4)} miles")
        elif choice == '2':
            print(f"{length} miles = {round(length / 0.621371, 4)} km")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose option (1/2): ")

    try:
        weight = float(input("Enter value: "))
        if choice == '1':
            print(f"{weight} kg = {round(weight * 2.20462, 4)} lbs")
        elif choice == '2':
            print(f"{weight} lbs = {round(weight / 2.20462, 4)} kg")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

def temp_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose option (1/2): ")

    try:
        temp = float(input("Enter temperature: "))
        if choice == '1':
            print(f"{temp}°C = {round((temp * 9/5) + 32, 2)}°F")
        elif choice == '2':
            print(f"{temp}°F = {round((temp - 32) * 5/9, 2)}°C")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

def unit_converter():
    print("********** Unit Converter **********")
    while True:
        print("\nMain Menu:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Choose category (1-4): ")

        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temp_converter()
        elif choice == '4':
            print("Thanks for using the Unit Converter!")
            break
        else:
            print("Invalid choice. Try again.")

        user_choice = input("\nDo you want to convert another unit? (Y/N): ").strip().upper()
        if user_choice != 'Y':
            print("Thank You!")
            break

unit_converter()
