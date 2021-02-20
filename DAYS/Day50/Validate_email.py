import re
Regex = r"[^@]+@[^@]+\.[^@]+"
Email = input("Enter Email: ")
if not re.match(Regex, Email):
    print("Invalid Email...")
else:
    print("Valid Email")
