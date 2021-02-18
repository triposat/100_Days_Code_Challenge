import validators
valid = validators.url("https://github.com/Iamtripathisatyam")
if valid:
    print("Valid URL")
else:
    print("Invalid URL")
