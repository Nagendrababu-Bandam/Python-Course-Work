# Day-12: Number guessing
secret = 7
guess = int(input("Guess a number from 1 to 10: "))
while guess != secret:
    print("Try again.")
    guess = int(input("Guess a number from 1 to 10: "))
print("Correct!")

# Sample Output:
# Guess a number from 1 to 10: 5
# Try again.
# Guess a number from 1 to 10: 7
# Correct!
