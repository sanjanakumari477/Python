#  empty list
numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)  # Add the number to the list

print("\nNumbers in the list:", numbers)

# Calculate sum, maximum, and average
total = sum(numbers)
maximum = max(numbers)
average = total / len(numbers)

# Display the results
print(f"Sum: {total}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")
