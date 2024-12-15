import hashlib

class MessagingApp:
    def __init__(self):
        self.users = {}  # Stores username: hashed_password
        self.messages = {}  # Stores username: list_of_messages

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        username = input("Enter a username: ").strip()
        if not username:
            print("Username cannot be empty. Try again.")
            return
        if username in self.users:
            print("Username already exists. Try again.")
            return
        password = input("Enter a password: ").strip()
        if not password:
            print("Password cannot be empty. Try again.")
            return
        self.users[username] = self.hash_password(password)
        self.messages[username] = []
        print("Registration successful!")

    def login(self):
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        hashed_password = self.hash_password(password)

        if self.users.get(username) == hashed_password:
            print(f"Welcome, {username}!")
            self.user_menu(username)
        else:
            print("Invalid username or password. Try again.")

    def send_message(self, sender):
        recipient = input("Enter the recipient's username: ").strip()
        if recipient not in self.users:
            print("Recipient not found. Please try again.")
            return
        message = input("Enter your message: ").strip()
        if not message:
            print("Message cannot be empty. Try again.")
            return
        self.messages[recipient].append((sender, message))
        print("Message sent successfully!")

    def view_message(self, username):
        user_messages = self.messages.get(username, [])
        if not user_messages:
            print("No messages found.")
            return
        print("Your messages:")
        for sender, message in user_messages:
            print(f"From {sender}: {message}")

    def user_menu(self, username):
        while True:
            print("\nUser Menu:")
            print("1. Send a message")
            print("2. View messages")
            print("3. Logout")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.send_message(username)
            elif choice == "2":
                self.view_message(username)
            elif choice == "3":
                print(f"Goodbye, {username}!")
                break
            else:
                print("Invalid choice. Try again.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = MessagingApp()
    app.main_menu()
