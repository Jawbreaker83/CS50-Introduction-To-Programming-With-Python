# Cheeck the validity of an email address.  The re library in python contains regular expressions.
import re

email = input("What is your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|org)", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# [^@] means any character except an @ sign and the + to the right means as many or more can follow

    

