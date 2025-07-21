import json

new_student = {
    "name": "Shahzoda", 
    "surname": "Nazarova", 
    "age": 22
}


with open('students.json', 'r') as f:
    students = json.load(f)


students.append(new_student)


with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)
