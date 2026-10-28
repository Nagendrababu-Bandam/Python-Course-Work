# Day-18: Functions - *args

def add_numbers(*numbers):
    print("Sum:", sum(numbers))

add_numbers(10, 20)
add_numbers(1, 2, 3, 4)

# Output:
# Sum: 30
# Sum: 10
