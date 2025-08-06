import numpy as 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the elements row-wise:")

# Input matrix elements
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)
np_matrix = np.array(matrix)

print("\nMatrix:")
print(np_matrix)


total_sum = np.sum(np_matrix)
print(f"\nSum of all elements in the matrix: {total_sum}")
