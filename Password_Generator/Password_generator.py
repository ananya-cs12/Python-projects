import random

def password(length, include_numbers=True, include_specials=True, skip_similar=True):
    
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    specials = '!@#$%^&*()-_=+[]{};:,.<>?/|'

    
    similar = 'oO0l1I'

    
    characters = lowercase + uppercase

    if include_numbers:
        characters += numbers
    if include_specials:
        characters += specials

   
    if skip_similar:
        for ch in similar:
            characters = characters.replace(ch, '')

    
    if characters == '':
        return "Error: No characters to choose from."

    
    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("**********Welcome to the Password Generator!***********")

    
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
    add_numbers = input("Include numbers? (Y/N): ").strip().lower()
    add_specials = input("Include special characters? (Y/N): ").strip().lower()
    remove_similar = input("Exclude similar-looking characters (O, 0, l, 1)? (Y/N): ").strip().lower()

    
    final_password = password(length,add_numbers == 'y',add_specials == 'y',remove_similar == 'y')
    print("\nYour generated password is:")
    print(final_password)

main()
