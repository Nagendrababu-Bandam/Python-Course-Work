# Day-09: Dictionary Basics
student = {"name": "Ravi", "age": 20, "course": "Python"}
print(student)
print("Name:", student["name"])
print("Age:", student.get("age"))
student["marks"] = 85
student["age"] = 21
print("Updated:", student)

# Output:
# {'name': 'Ravi', 'age': 20, 'course': 'Python'}
# Name: Ravi
# Age: 20
# Updated: {'name': 'Ravi', 'age': 21, 'course': 'Python', 'marks': 85}
