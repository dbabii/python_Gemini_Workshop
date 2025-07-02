class Country:
# create three keyword arguments
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq
# added additional method to convert km to ml
    def size_miles_sq(self, conversion_rate=0.621371):
        return self.size_kmsq * conversion_rate ** 2
# added string method
    def __str__(self):
        label = self.name
        if self.population:
            label = '%s, population: %s' % (label, self.population) # use 'printf' style
        if self.size_kmsq:
            label = f'{label}, size_kmsq: {self.size_kmsq}' # use f-string style
        return label

usa = Country(name='United States of America', size_kmsq=9.8e6) # e6 = 10^6
print(usa.__dict__)
# create a new object of Country class
algeria = Country(name='Algeria', size_kmsq=2.382e6)
print(algeria.size_miles_sq())
# change the default parameter
print(algeria.size_miles_sq(conversion_rate=0.6))
print(algeria.size_miles_sq()) # the default parameter remains unchanged

## string method with two parameters
# chad = Country(name='Chad', size_kmsq=1.284e6)
# chad = Country(name='Chad', population=19.32e6)
## string method with all parameters
chad = Country(name='Chad', population=19.32e6, size_kmsq=1.284e6)
print(chad)