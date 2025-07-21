import json

students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]


json_string = json.dumps(students,indent = 4)


with open("students.json", "w") as file:
    file.write(json_string)

