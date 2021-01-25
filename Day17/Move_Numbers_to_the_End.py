def Move_at_end(Test_String):
    one_Half = ''.join([ele for ele in Test_String if ele.isdigit()])
    second_half = ''.join([ele for ele in Test_String if not ele.isdigit()])
    second_half += one_Half
    return second_half


Test_String = input("Enter a String: ")
print(Move_at_end(Test_String))
