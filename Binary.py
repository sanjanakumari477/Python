# Program to convert a number into binary form

# Get input from user
num = int(input("Enter a number: "))

# Convert to binary using bin() and remove '0b' prefix
binary = bin(num)[2:]

# Display the result
print(f"The binary form of {num} is: {binary}")
