# 1 Problem - Solving with Python
input_string = input("Enter a list of integers separated by spaces: ")

numbers = list(map(int, input_string.split()))

unique_numbers = list(set(numbers))

# Sort the list in descending order
unique_numbers.sort(reverse=True)

# Print the result
print("Sorted list without duplicates:", unique_numbers)



