import re
File_names = ["gfg.html", "geeks.xml",
              "computer.txt", "geeksforgeeks.jpg", "hey.png"]
Extension = input("Enter Extension: ")
Final = "\."+Extension+"$"
for file in File_names:
    match = re.search(Final, file)
    if match:
        print("File is:", file)
