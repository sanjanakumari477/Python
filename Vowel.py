# Get input from the user
text = input("Enter a string: ")

# Convert to lowercase for easy comparison
text = text.lower()

# Define a set of vowels
vowels = "aeiou"

# Initialize count
count = 0

# Loop through each character
for char in text:
    if char in vowels:
        count += 1

# Display the result
print("Number of vowels:", count)
