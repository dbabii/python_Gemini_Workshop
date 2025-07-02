import datetime

class Diary:
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas

# use DRY principle
    @staticmethod
    def format_date(date):
        return date.strftime('%d-%b-%y')

# change date format to dd-mm-yy
    def show_birthday(self):
        return self.format_date(self.birthday)

    def show_christmas(self):
        return self.format_date(self.christmas)

# create an object
my_diary = Diary(datetime.date(2020, 5 , 14), datetime.date(2020,12,25))
print(my_diary.show_birthday())
print(my_diary.show_christmas())