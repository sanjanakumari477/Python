# Program: Working with Sets in Python

# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Adding elements to the set
numbers.add(6)
numbers.add(3)  # Duplicate won't be added

# Removing an element
numbers.remove(4)

# Checking if an element exists
if 2 in numbers:
    print("2 is in the set")

# Performing set operations
even_numbers = {2, 4, 6, 8}
print("Union:", numbers.union(even_numbers))
print("Intersection:", numbers.intersection(even_numbers))
print("Difference:", numbers.difference(even_numbers))

# Printing final set
print("Final Set:", numbers)
