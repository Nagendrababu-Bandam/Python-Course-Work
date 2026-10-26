# Day-09: Dictionary Programs
marks = {"Maths": 90, "Science": 85, "English": 88}
print("Subjects:", list(marks.keys()))
print("Marks:", list(marks.values()))
print("Total:", sum(marks.values()))
print("Average:", sum(marks.values()) / len(marks))

# Output:
# Subjects: ['Maths', 'Science', 'English']
# Marks: [90, 85, 88]
# Total: 263
# Average: 87.66666666666667
