# Dictionary Programs

student = {"name": "Nagendra", "age": 22, "course": "Python"}
print(student)

# Output:
# {'name': 'Nagendra', 'age': 22, 'course': 'Python'}

# 2.Access dictionary values
student = {"name": "Nagendra", "age": 22, "course": "Python"}
print(student["name"])
print(student["age"])

# Output:
# Nagendra
# 22

# 3.Add a new item to a dictionary
student = {"name": "Nagendra", "age": 22}
student["city"] = "Telangana"
print(student)

# Output:
# {'name': 'Nagendra', 'age': 22, 'city': 'Telangana'}

# 4.Update a dictionary value
student = {"name": "Nagendra", "age": 22}
student["age"] = 23
print(student)

# Output:
# {'name': 'Nagendra', 'age': 23}

# 5.Delete an item from a dictionary
student = {"name": "Nagendra", "age": 22, "course": "Python"}
del student["age"]
print(student)

# Output:
# {'name': 'Nagendra', 'course': 'Python'}