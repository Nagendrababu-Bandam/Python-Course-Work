# Day-08: List vs Tuple
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[0] = 100
print("List can be changed:", my_list)
print("Tuple:", my_tuple)
# Tuples are immutable (their items cannot be reassigned).

# Output:
# List can be changed: [100, 2, 3]
# Tuple: (1, 2, 3)
