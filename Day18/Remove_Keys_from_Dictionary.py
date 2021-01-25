def Remove_Keys(Test_dict, Remove_Value):
    return {key: value for key, value in Test_dict.items() if key != Remove_Value}


N_value = int(input("Enter n: "))
Test_dict = {}
for i in range(N_value):
    key = input("Key: ")
    Value = int(input("Value: "))
    Test_dict[key] = Value
Remove_Value = input("Which Key to Delete: ")
print(Remove_Keys(Test_dict, Remove_Value))