students = []

with open ('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        student = {"name":name, "house": house}
        students.append(student)
#The lambda function (an anonomys function) is the equivalent to writing the get_name function writtin in v5
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")