import numpy as np

# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize matrix
matrix = []

print("Enter the elements row-wise:")

# Input matrix elements
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

# Convert to NumPy array
np_matrix = np.array(matrix)

# Display matrix
print("\nMatrix:")
print(np_matrix)

# Calculate sum of matrix
total_sum = np.sum(np_matrix)
print(f"\nSum of all elements in the matrix: {total_sum}")
