from datetime import date, time, datetime

today = date.today()
print(today)

now = datetime.now()
print(now)

print(f"currnt Year : {today.year}")
print(f"currnt Month : {today.month}")
print(f"currnt Day : {today.day}")