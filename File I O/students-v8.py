import csv
students = []

with open ('students-v3.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], 
        "home": row["home"]})

#The lambda function (an anonomys function) is the equivalent to writing the get_name function writtin in v5
for student in sorted(students, 
    key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")