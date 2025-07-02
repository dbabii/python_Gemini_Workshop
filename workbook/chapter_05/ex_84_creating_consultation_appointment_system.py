import datetime

class Person:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

class Baby(Person):
    def speak(self):
        print('Blah blah blah')

class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)

class Calendar():
    def book_appointment(self, date):
        print('Booking appointment for date %s' % date)
# defying classes without adding or customizing its methods/attrs
class OrganizedBaby(Baby, Calendar):
    pass

class OrganizedAdult(Adult, Calendar):
    pass

andres = OrganizedAdult('Andres', 'Gomez')
boris = OrganizedBaby('Boris', 'Bumblebutton')
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2025, 8, 10))