import getpass

# Ask the user to enter a username and password
username = input("Enter your username: ")
password = getpass.getpass("Enter your password (it will be hidden): ")

# Print confirmation (not the actual password)
print("\nAccount created successfully!")
print(f"Username: {username}")
print("Password is securely hidden.")
