A dictionary is an unordered, mutable collection of key-value pairs. Keys must be unique and hashable, while values can be of any type.

List/Tuple → Ordered collections indexed by position

Dictionary → Indexed by keys
-------------------------------------------------------------------------------------------------------------------------------------


# How do you create an empty dictionary?
my_dict = {}
# or
my_dict = dict()

---------------------------------------------------------------------------------------------------------------------------------

# How do you access a value from a dictionary?
student = {"name": "Alice", "age": 22}
print(student["name"])  # Alice


----------------------------------------------------------------------------------------------------------------------------

# How do you add a new key-value pair to a dictionary?
student["course"] = "BCA"

--------------------------------------------------------------------------------------------------------------------------

# How do you update the value of an existing key?
student["age"] = 23

-----------------------------------------------------------------------------------------------------------------------------

# How do you delete a key-value pair from a dictionary?
del student["course"]
# or
student.pop("age")

-------------------------------------------------------------------------------------------------------------------------------------
