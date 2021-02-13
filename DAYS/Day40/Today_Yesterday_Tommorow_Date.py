from datetime import date, datetime, timedelta

Present_Day = datetime.now()
Yesterday = Present_Day-timedelta(1)
Tommorow = Present_Day+timedelta(1)

print(f"Today Date: {Present_Day.strftime('%d-%m-%Y')}")
print(f"Yesterday Date: {Yesterday.strftime('%d-%m-%Y')}")
print(f"Tommorow Date: {Tommorow.strftime('%d-%m-%Y')}")
