# Day-11: Nested if
x = int(input("Enter x: "))
if x > 5:
    if x > 15:
        print("x is greater than 15")
    else:
        print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")

# Sample Output:
# Enter x: 10
# x is greater than 5 but not greater than 15
