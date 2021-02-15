# Approach 1:

def Time_Difference(h1, m1, h2, m2):
    Time_1 = h1*60+m1
    Time_2 = h2*60+m2
    if Time_1 == Time_2:
        print("Both are Same")
        return
    else:
        Diff = Time_2-Time_1

    Hour = int(Diff/60)
    Minutes = Diff % 60
    print(f"Difference: {Hour} : {Minutes}")


if __name__ == "__main__":
    Time_Difference(7, 20, 9, 45)
    Time_Difference(15, 23, 18, 54)
    Time_Difference(16, 20, 16, 20)


# Approach 2:    
    
from datetime import datetime
Time_1 = '10:33:26'
Time_2 = '11:15:49'
FMT = '%H:%M:%S'
Diff = datetime.strptime(Time_2, FMT) - datetime.strptime(Time_1, FMT)
print(Diff)
