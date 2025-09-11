phonebook = {}

while True:
    print("------------------Phonebook-------------------")
    print("Select one of below actions: ")
    print("1. Create contact")
    print("2. Search contacts")
    print("3. View contacts")
    print("4. Quit")
    try:
        choice = int(input("Enter a number (1-4): "))
    except:
        print("Invalid input. please enter a number between 1-4.")
        continue
    if choice == 1:
        name = input("Enter contact Name: ").strip()
        try:
            number = int(input("Enter contact number: "))
        except:
            print("Numbers must be digits only")
            continue
        phonebook[name] = number
        print(f"{name}'s number is added to the phonebook successfuly.")

    elif choice == 2:
        search = input("Enter name/phone number: ")
        for name, number in phonebook.items():
            if search == name or search == str(number):
                print(f"{name}: {number}")
                break
        else:
            print("Not found!")

    elif choice == 3:
        if not phonebook:
            print(f"Phonebook is empty.")
        else:
            for name, number in phonebook.items():
                print("List of users: ")
                print(f"{name}: {number}")
    elif choice == 4:
        print("Good Bye!")
        break
