import datetime

class Diary:
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas

# change date format to dd-mm-yy
    def show_birthday(self):
        return self.birthday.strftime('%d-%b-%y')

    def show_christmas(self):
        return self.christmas.strftime('%d-%b-%y')

# create an object
my_diary = Diary(datetime.date(2020, 5 , 14), datetime.date(2020,12,25))
print(my_diary.show_birthday())
print(my_diary.show_christmas())