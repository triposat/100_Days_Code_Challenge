from datetime import datetime

Given_time = 1617301800

Result = datetime.fromtimestamp(Given_time).strftime("%d-%m-%Y")
print(Result)
