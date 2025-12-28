import json

class UserManager:
    def __init__(self):
        self.users = []

    def load_users(self, filename="users.json"):
        try:
            with open(filename, "r") as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []

    def save_users(self, filename="users.json"):
        with open(filename, "w") as f:
            json.dump(self.users, f, indent=4)

    def add_user(self, name, age, email):
        self.users.append({
            "name": name,
            "age": age,
            "email": email
        })
        self.save_users()

    def list_users(self):
        if not self.users:
            print("No users found.\n")
            return
        for user in self.users:
            print(f"{user['name']} | {user['age']} | {user['email']}")
        print()

    def show_report(self):
        if not self.users:
            print("No users available.\n")
            return

        avg_age = sum(u["age"] for u in self.users) / len(self.users)
        oldest = max(self.users, key=lambda x: x["age"])
        youngest = min(self.users, key=lambda x: x["age"])

        print(f"Average age: {avg_age:.2f}")
        print(f"Oldest: {oldest['name']} ({oldest['age']})")
        print(f"Youngest: {youngest['name']} ({youngest['age']})\n")

    def edit_user(self, name):
        for user in self.users:
            if user["name"] == name:
                age = input("New age (blank to skip): ")
                email = input("New email (blank to skip): ")

                if age:
                    user["age"] = int(age)
                if email:
                    user["email"] = email

                self.save_users()
                print("User updated.\n")
                return
        print("User not found.\n")

    def delete_user(self, name):
        for user in self.users:
            if user["name"] == name:
                self.users.remove(user)
                self.save_users()
                print("User deleted.\n")
                return
        print("User not found.\n")
