import os

def file_creator():
    if os.path.exists('students.json'):
        print('Bu fayl mavjud')
    else:
       with open('students.json','x') as f:
            f.write('[]')
            print('Fayl yaratildi')

file_creator()                