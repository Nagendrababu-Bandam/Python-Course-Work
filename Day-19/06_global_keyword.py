# Day-19: Scope - global Keyword

count = 5

def update_count():
    global count
    count = 10

update_count()
print(count)

# Output:
# 10
