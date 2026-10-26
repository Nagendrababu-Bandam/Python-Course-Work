# Day-16: Binary triangle
for i in range(1, 6):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()

# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
