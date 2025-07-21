import json
import csv

with open('students.json') as json_file:
    py = json.load(json_file)

with open('students.csv','x') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['Name', 'Surname', 'Age'])

    for student in py:
        writer.writerow([student['name'], student['surname'], student['age']])
    