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

class CustomDiary(Diary):
    def __init__(self, birthday, christmas, date_format):
        self.date_format = date_format
# use access to the parent class
        super().__init__(birthday, christmas)
# override format date
    def format_date(self, date):
        return date.strftime(self.date_format)

first_diary = CustomDiary(datetime.date(1985, 12, 1),
                          datetime.date(1985, 12, 25),
                          '%d-%b-%Y')

second_diary = CustomDiary(datetime.date(1958, 12, 1),
                           datetime.date(1965, 12,25),
                           '%Y/%m/%d')

print(first_diary.show_birthday())
print(second_diary.show_birthday())