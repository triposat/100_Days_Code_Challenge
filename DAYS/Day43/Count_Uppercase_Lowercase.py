import re


def Upper_Lower_Count(Test_string):
    Upper_Case = re.findall(r"[A-Z]", Test_string)
    Lower_Case = re.findall(r"[a-z]", Test_string)
    Numeric_Char = re.findall(r"[0-9]", Test_string)
    Special_Char = re.findall(r"[ ,.!?]", Test_string)
    print(f"Upper Case - {len(Upper_Case)}")
    print(f"Lower Case - {len(Lower_Case)}")
    print(f"Numeric Characters - {len(Numeric_Char)}")
    print(f"Special Characters Case - {len(Special_Char)}")


Test_string = "ThisIs100DaysofCodeChallenge !, 123"
Upper_Lower_Count(Test_string)
