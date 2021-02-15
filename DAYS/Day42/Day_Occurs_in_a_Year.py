import datetime
import calendar


def Day_Occur(Year):
    Days_list = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']

    Days_Count = [52 for i in range(7)]
    pos = 0
    First_day = datetime.datetime(Year, month=1, day=1).strftime("%A")
    pos = Days_list.index(First_day)
    if calendar.isleap(Year):
        Days_Count[pos] += 1
        Days_Count[(pos+1) % 7] += 1
    else:
        Days_Count[pos] += 1

    for days in range(7):
        print(f"{Days_list[days]} : {Days_Count[days]}")


Year = int(input("Enter a Year: "))
Day_Occur(Year)
