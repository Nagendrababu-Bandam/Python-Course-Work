# Day-14: Palindrome Number
number = input("Enter a number: ")
if number == number[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Sample Output:
# Enter a number: 121
# Palindrome
