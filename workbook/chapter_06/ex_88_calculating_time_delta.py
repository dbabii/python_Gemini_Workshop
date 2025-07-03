import datetime as dt

# create two datetime objects
d1 = dt.datetime(2025, 1, 12, 10, 50,
                 tzinfo=dt.timezone.utc)
d2 = dt.datetime(2025, 1, 14, 11, 20,
                 tzinfo=dt.timezone.utc)
# find out time delta in seconds
td = d2 - d1
print(td.total_seconds())

# diff between ISO format and as is
print(d2.isoformat())
print(d2)

# isoformat time now
d3 = dt.datetime.now(dt.timezone.utc)
print(d3.isoformat())