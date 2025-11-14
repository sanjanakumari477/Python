# Take input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd = 1
# Loop from 1 to the smallest of the two numbers
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i  # Update gcd

print(f"The GCD of {a} and {b} is: {gcd}")
