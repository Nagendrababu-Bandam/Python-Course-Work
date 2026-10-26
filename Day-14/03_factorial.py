# Day-14: Factorial
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Please enter a non-negative integer")
else:
    result = 1
    for i in range(1, number + 1):
        result *= i
    print("Factorial:", result)

# Sample Output:
# Enter a non-negative integer: 5
# Factorial: 120
