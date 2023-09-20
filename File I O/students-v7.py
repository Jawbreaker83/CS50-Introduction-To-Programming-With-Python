import csv
students = []

with open ('students-v2.csv') as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

#The lambda function (an anonomys function) is the equivalent to writing the get_name function writtin in v5
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")