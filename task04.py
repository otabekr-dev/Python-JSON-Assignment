import json

name = input('Ism kiritng:')
surname = input('Familiya kiritng:')
age = int(input('Yosh kiritng:'))

new_student = {
    'name': name,
    'surname': surname,
    'age': age
}

with open('students.json', 'r') as f:
    students = json.load(f)


students.append(new_student)


with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)