import datetime

Given_time = "02/04/2021"

Semi_Result = datetime.datetime.strptime(Given_time, "%d/%m/%Y")
Result = datetime.datetime.timestamp(Semi_Result)
print(Result)
