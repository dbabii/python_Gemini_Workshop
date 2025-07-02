class Person():
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.second_name)


customer = Person('Mary', 'Lou')
print(customer.full_name)

# get an error for the following code because there is no used a setter
customer.full_name = 'Mary Schnidt'