import json 
from pprint import pprint


with open('students.json') as f:
    py = json.load(f)

filtered = list(filter(lambda student:student['age'] > 20, py))
pprint(filtered)