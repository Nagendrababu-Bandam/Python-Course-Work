# Day-14: Armstrong Number
number = input("Enter a non-negative integer: ")
power = len(number)
total = sum(int(digit) ** power for digit in number)
if total == int(number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Sample Output:
# Enter a non-negative integer: 153
# Armstrong number
