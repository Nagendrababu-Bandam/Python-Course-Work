# Day-10: if-elif-else statement
marks = float(input("Enter marks (0-100): "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 0:
    print("Grade D")
else:
    print("Invalid marks")

# Sample Output:
# Enter marks (0-100): 82
# Grade B
