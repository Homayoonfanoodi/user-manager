from user_manager import UserManager

manager = UserManager()
manager.load_users()

while True:
    print("1. Add user")
    print("2. Show report")
    print("3. List users")
    print("4. Edit user")
    print("5. Delete user")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        email = input("Email: ")
        manager.add_user(name, age, email)

    elif choice == "2":
        manager.show_report()

    elif choice == "3":
        manager.list_users()

    elif choice == "4":
        name = input("Name to edit: ")
        manager.edit_user(name)

    elif choice == "5":
        name = input("Name to delete: ")
        manager.delete_user(name)

    elif choice == "6":
        print("Bye 👋")
        break

    else:
        print("Invalid choice\n")
