import json

input_file = open('students.json')

with input_file:
    py = json.load(input_file)

for student in py:
    print(student['name'],'-',student['age'])    