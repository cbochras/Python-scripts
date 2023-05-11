import hashlib

# Define a dictionary to store the passwords
passwords = {}

def get_hash(password):
    """
    Returns the SHA256 hash of the given password
    """
    return hashlib.sha256(password.encode()).hexdigest()

def add_password():
    """
    Add a new password to the password dictionary
    """
    website = input("Enter the website name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    passwords[website] = {"username": username, "password": get_hash(password)}

def get_password():
    """
    Retrieve a password from the password dictionary
    """
    website = input("Enter the website name: ")
    if website in passwords:
        username = passwords[website]["username"]
        password_hash = passwords[website]["password"]
        password = input("Enter the password: ")
        if get_hash(password) == password_hash:
            print("Username:", username)
            print("Password:", password)
        else:
            print("Incorrect password")
    else:
        print("Website not found")

# Main loop
while True:
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
