# Cheeck the validity of an email address.  The re library in python contains regular expressions.
import re

email = input("What is your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

    

