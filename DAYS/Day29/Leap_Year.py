import calendar


def Leap_Year(Test_input):
    count = 0
    Result = []
    while count < 15:
        if calendar.isleap(Test_input):
            Result.append(Test_input)
            count += 1
        Test_input += 1
    return Result

Test_input = int(input("Enter Year: "))
print(Leap_Year(Test_input))
