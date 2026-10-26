# Day-02: POP vs OOP (simple example)
# POP = Procedure-Oriented Programming: organizes code around functions/procedures.
# OOP = Object-Oriented Programming: organizes code around classes and objects.

# Procedure-oriented style
def add_numbers(a, b):
    return a + b

print("POP-style function result:", add_numbers(2, 3))

# Object-oriented style
class Calculator:
    def add(self, a, b):
        return a + b

calculator = Calculator()
print("OOP-style method result:", calculator.add(2, 3))

# Output:
# POP-style function result: 5
# OOP-style method result: 5
