# Day-14: Prime Number
number = int(input("Enter a number: "))
if number < 2:
    print("Not prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

# Sample Output:
# Enter a number: 7
# Prime
