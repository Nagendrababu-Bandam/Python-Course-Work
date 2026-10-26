# List programs
# List: A collection of items. We use square brackets []. A list can be changed.

# 1: Print a list
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Output:
# ['apple', 'banana', 'mango']
# apple
# banana
# mango

# 2: Add an item to a list
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# Output: [10, 20, 30, 40]

# 3: Remove an item
numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)

# Output: [10, 30, 40]

# 4: Print list items using a loop
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango