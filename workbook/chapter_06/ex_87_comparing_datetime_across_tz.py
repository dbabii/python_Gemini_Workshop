import datetime
from dateutil import tz

# create a first datetime for Madrid
d1 = datetime.datetime(1989, 4, 24, hour=11,
                       tzinfo=tz.gettz("Europe/Madrid"))
# create a second date time for Los Angeles
d2 = datetime.datetime(1989, 4, 24, hour=8,
                       tzinfo=tz.gettz("America/Los_Angeles"))

# comparing
print(d1.hour > d2.hour)
print(d1 > d2)

# convert to different timezone
d2_madrid = d2.astimezone(tz.gettz("Europe/Madrid"))
print(d2_madrid.hour)

