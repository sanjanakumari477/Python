numbers = input("Enter numbers separated by space: ")
num_list = list(map(int, numbers.split()))

largest = max(num_list)
smallest = min(num_list)

print("Largest number:", largest)
print("Smallest number:", smallest)
