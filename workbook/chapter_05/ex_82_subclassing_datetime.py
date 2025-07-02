import datetime

class MyDate(datetime.date):
    def add_days(self, n):
        return self + datetime.timedelta(n)

d = MyDate(2025, 7, 2)
print(d.add_days(30))
print(d.add_days(60))