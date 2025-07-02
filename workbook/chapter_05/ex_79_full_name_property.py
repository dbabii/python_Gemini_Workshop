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