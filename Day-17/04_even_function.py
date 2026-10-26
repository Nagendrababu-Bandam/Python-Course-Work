# Day-17: Function to check even or odd
def is_even(number):
    return number % 2 == 0

value = int(input("Enter a number: "))
if is_even(value):
    print("Even")
else:
    print("Odd")

# Sample Output:
# Enter a number: 4
# Even
