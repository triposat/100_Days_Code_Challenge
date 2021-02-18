from itertools import permutations
import re
Test_URL = 'https://www.geeksforgeeks.org/'
Sample1 = "(\w+)://"
Sample2 = "://www.([\w\-\.]+)"
print("Protocol: " + "".join(re.findall(Sample1, Test_URL)))
print("Host Name: " + "".join(re.findall(Sample2, Test_URL)))
