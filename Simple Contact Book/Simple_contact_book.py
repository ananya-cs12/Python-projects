def add_contact():
    with open("contacts.txt", "a") as file:
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        file.write(f"{name}\t{phone}\t{email}\n")
        print("Contact added successfully!\n")

def view_contacts():
    print("\n------ All Contacts ------")
    try:
        with open("contacts.txt", "r") as file:
            l = file.readlines()
            if not l:
                print("No contacts found.\n")
            else:
                for i in l:
                    name, phone, email = i.strip().split("\t")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
    except FileNotFoundError:
        print("No contacts file found.\n")

def search_contact():
    search = input("Enter name or phone to search: ").strip().lower()
    found = False
    try:
        with open("contacts.txt", "r") as F1:
            for i in F1:
                if search in i.lower():
                    name, phone, email = i.strip().split("\t")
                    print(f"Found — Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
        if not found:
            print("No matching contact found.")
    except FileNotFoundError:
        print("No contacts file found.\n")

def delete_contact():
    value = input("Enter name or phone to delete: ").strip().lower()
    updated = []
    deleted = False
    try:
        with open("contacts.txt", "r") as F1:
            for i in F1:
                if value not in i.lower():
                    updated.append(i)
                else:
                    deleted = True
        with open("contacts.txt", "w") as F1:
            F1.writelines(updated)
        if deleted:
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts file found.\n")

def edit_contact():
    value = input("Enter name or phone to edit: ").strip().lower()
    updated = []
    edited = False
    try:
        with open("contacts.txt", "r") as F1:
            for i in F1:
                if value in i.lower():
                    print("Found contact to edit:")
                    name, phone, email = i.strip().split("\t")
                    print(f"Current — Name: {name}, Phone: {phone}, Email: {email}")
                    new_name = input("Enter new name (or press Enter to keep current): ").strip() or name
                    new_phone = input("Enter new phone (or press Enter to keep current): ").strip() or phone
                    new_email = input("Enter new email (or press Enter to keep current): ").strip() or email
                    updated.append(f"{new_name}\t{new_phone}\t{new_email}\n")
                    edited = True
                else:
                    updated.append(i)
        with open("contacts.txt", "w") as F1:
            F1.writelines(updated)
        if edited:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts file found.\n")

def main():
    while True:
        print("\n=====Contact Book Menu=====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            edit_contact()
        elif choice == '6':
            print("Exited Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
