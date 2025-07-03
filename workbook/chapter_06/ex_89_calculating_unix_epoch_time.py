import datetime as dt
import time

time_now = time.time()
datetime_now = dt.datetime.now(dt.timezone.utc)

print(time_now, datetime_now)
# show when UNIX time was started
epoch = datetime_now - dt.timedelta(seconds=time_now)
print(epoch)