import json

with open('students.json') as json_file:
    students = json.load(json_file)

sorted_ones = list(sorted(students, key= lambda student:int(student['age'])))

for student in sorted_ones:
    print(student['name'], student['surname'], student['age'])
