#t1
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("5 days ago:", new_date)
#t2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#t3
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", without_microseconds)
#t4
from datetime import datetime

date1 = datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime(2026, 2, 25, 12, 30, 0)

difference = date2 - date1

print("Difference in seconds:", difference.total_seconds())