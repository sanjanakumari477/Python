rows = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for printing stars
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row
