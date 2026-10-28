# Day-19: Recursion - Countdown

def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(3)

# Output:
# 3
# 2
# 1
# Done!
