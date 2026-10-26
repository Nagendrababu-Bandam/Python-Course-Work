# Set programs
# Set: A collection of unique items. We use curly brackets {}. 
# Duplicate values are automatically removed.

# 1: Print a set
numbers = {10, 20, 30, 20, 10}
print(numbers)

# Output: The set contains only 10, 20, 30 (the order may vary).

# 2: Add an item to a set
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# Output: A set containing 10, 20, 30, 40.

# 3: Remove an item from a set
numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)

# Output: A set containing 10, 30, 40.

# 4: Find common items in two sets
a = {10, 20, 30}
b = {20, 30, 40}
print(a.intersection(b))

# Output: {20, 30}