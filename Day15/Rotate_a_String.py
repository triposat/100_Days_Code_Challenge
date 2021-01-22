def Rotate_String(Test_string, n):
    Left_First = Test_string[0:n]
    Left_Second = Test_string[n:]
    Right_First = Test_string[0:len(Test_string)-n]
    Right_Second = Test_string[len(Test_string)-n:]
    return f"Left Rotation: {Left_Second+Left_First}\nRight Rotation: {Right_Second+Right_First}"


Test_string = input("Enter a String: ")
n = int(input("Upto: "))
print(Rotate_String(Test_string, n))
