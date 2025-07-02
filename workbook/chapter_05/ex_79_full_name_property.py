class Person():
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.second_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.second_name = last


customer = Person('Mary', 'Lou')
print(customer)
print(customer.full_name)

# get an error for the following code because there is no used a setter
# change the full name of the customer. Previous data has been gone
customer.full_name = 'Mary Schmidt'
print(customer)
print(customer.full_name)
print(customer.second_name)

class Baby(Person):
    def speak(self):
        print('Blah blah blah')

class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)

jess = Baby('Jessie', 'McDonald')
tom = Adult('Thomas', 'Smith')

jess.speak()
tom.speak()

class TwoNamesPerson(Person):
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.second_name)
# overriding full name setter method and add the possibility to have two names
    @full_name.setter
    def full_name(self, name):
        names = name.split(' ')
        if len(names) > 2:
            self.first_name = ' '.join(names[:2])
        elif len(names) == 2:
            self.first_name = names[0]
        self.second_name = names[-1]

my_person = TwoNamesPerson('Joanna', 'Smith')
my_person.full_name = 'Joanna Anne Smith'
print(my_person.first_name)
print(my_person.second_name)