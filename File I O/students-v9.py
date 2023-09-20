import csv

name = input("what is your name? ")
home = input ("Where is your home? ")

with open("students-v4.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

