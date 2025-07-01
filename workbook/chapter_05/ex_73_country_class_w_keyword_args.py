class Country:
# create three keyword arguments
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

usa = Country(name='United States of America', size_kmsq=9.8e6) # e6 = 10^6

print(usa.__dict__)