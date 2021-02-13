from time import time


def Convert_Format(Time):
    if Time[:2] == "12" and Time[-2:] == "AM":
        return "00"+Time[2:-2]
    elif Time[-2:] == "AM":
        return Time[:-2]
    elif Time[:2] == "12" and Time[-2:] == "PM":
        return Time[:-2]
    else:
        return str(int(Time[:2])+12)+Time[2:]


Time = "09:05:52 PM"
print(Convert_Format(Time))
