# Day-08: List Basics
numbers = [10, 20, 30, 40]
print(numbers)
print("First:", numbers[0])
numbers.append(50)
numbers.insert(1, 15)
print("Updated:", numbers)
numbers.remove(30)
print("After remove:", numbers)

# Output:
# [10, 20, 30, 40]
# First: 10
# Updated: [10, 15, 20, 30, 40, 50]
# After remove: [10, 15, 20, 40, 50]
