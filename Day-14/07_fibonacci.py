# Day-14: Fibonacci Series
n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(max(0, n)):
    print(a, end=" ")
    a, b = b, a + b
print()

# Sample Output:
# How many terms? 6
# 0 1 1 2 3 5
