# Armstrong number check program

# Get input from the user
num = int(input("Enter a number: "))

# Convert number to string to count digits
num_str = str(num)
n = len(num_str)

# Calculate sum of digits raised to the power n
sum_of_powers = sum(int(digit) ** n for digit in num_str)

# Check if it's an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
