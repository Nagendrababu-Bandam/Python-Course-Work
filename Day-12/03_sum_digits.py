# Day-12: Sum of digits
number = int(input("Enter a positive integer: "))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Sum of digits:", total)

# Sample Output:
# Enter a positive integer: 123
# Sum of digits: 6
