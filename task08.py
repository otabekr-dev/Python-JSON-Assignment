import json

with open('students.json') as f:
    students = json.load(f)


ages = []
for student in students:
    ages.append(int(student['age']))


old_one = max(ages, key=lambda age:age)

print("Eng katta yosh:", old_one)
