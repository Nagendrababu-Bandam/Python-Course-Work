# Day-18: Functions - **kwargs

def show_details(**details):
    for key, value in details.items():
        print(key, ":", value)

show_details(name="Ravi", age=20)

# Output:
# name : Ravi
# age : 20
