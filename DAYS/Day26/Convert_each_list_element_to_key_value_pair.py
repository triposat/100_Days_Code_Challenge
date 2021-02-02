def Key_Value_Pair(Test_list):
    Result = dict()
    for elements in Test_list:
        Mid = len(str(elements))//2
        Key = int(str(elements)[:Mid])
        Value = int(str(elements)[Mid:])
        Result[Key] = Value
    return Result


Test_list = [2323, 82, 129388, 234, 95]
print(Key_Value_Pair(Test_list))
