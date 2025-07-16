users = {
    "saad": {
        "username": "saad007",
        "email": "saad007@gmail.com",
        "password": "saad007",
        "age": 24,
        "gender": "male"
    },
    "arham": {
        "username": "arham123",
        "email": "arham123@gmail.com",
        "password": "arham123",
        "age": 21,
        "gender": "male"
    },
    "hamdan": {
        "username": "hamdan887",
        "email": "hamdan887@gmail.com",
        "password": "hamdan887",
        "age": 27,
        "gender": "male"
    },
    "nouman": {
        "username": "muhammad nouman",
        "email": "muhammad nouman@gmail.com",
        "password": "nouman123",
        "age": 26,
        "gender": "male"
    }
}


# === Function to Display All Users ===
def show_all_users():
    print("\n--- All Users ---")
    for name, details in users.items():
        print(f"{name.upper()} => {details}")
    print("------------------\n")


# === Function to Login ===
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for name, info in users.items():
        if info["username"] == username and info["password"] == password:
            print(f"\n✅ Welcome back, {username}!")
            print(f"👤 Name: {name.capitalize()}")
            print(f"📧 Email: {info['email']}")
            print(f"🎂 Age: {info['age']}")
            print(f"⚧ Gender: {info['gender'].capitalize()}")
            return
    print("❌ Invalid username or password.\n")


# === Function to Update Info ===
def update_user_info():
    name = input("Enter the name of user to update info: ").strip().lower()
    if name in users:
        new_email = input("New Email: ")
        new_username = input("New Username: ")
        users[name]["email"] = new_email
        users[name]["username"] = new_username
        print("✅ Info updated successfully!\n")
    else:
        print("❌ User not found!\n")


# === Function to Delete a User ===
def delete_user():
    name = input("Enter name to delete: ").strip().lower()
    if name in users:
        users.pop(name)
        print(f"🗑️ User '{name}' deleted successfully!\n")
    else:
        print("❌ User not found!\n")


# === Main Menu ===
def main_menu():
    while True:
        print("\n======== USER SYSTEM MENU ========")
        print("1. Login")
        print("2. Show All Users")
        print("3. Update User Info")
        print("4. Delete a User")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            login_user()
        elif choice == "2":
            show_all_users()
        elif choice == "3":
            update_user_info()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# === Run Program ===
main_menu()