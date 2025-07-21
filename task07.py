import json

with open('students.json') as f:
    students = json.load(f)


ages = []
for student in students:
    ages.append(int(student['age']))


avg = sum(ages) / len(ages)

print("O'rtacha yosh:", avg)
