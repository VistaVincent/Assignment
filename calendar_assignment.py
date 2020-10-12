import calendar
import datetime

now = datetime.datetime.now()
y = int(now.year)
m = int(now.month)

print(calendar.month(y, m))