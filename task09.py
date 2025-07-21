import json

with open('students.json') as json_file:
    students = json.load(json_file)

amount = 0

for student in students:
    amount += 1

print(f'Talabalar soni {amount} ta')    