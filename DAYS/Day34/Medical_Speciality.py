Test_dict = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
Test_list = [101, 'P', 102, 'E', 302, 'P', 305,
             'P', 401, 'E', 656, 'O', 987, 'E', 999, 'E']
Result = {}
for items in Test_list:
    if isinstance(items, str):
        Result[items] = Test_list.count(items)
print(max(Result, key=Result.get))
print(Test_dict[max(Result, key=Result.get)])
