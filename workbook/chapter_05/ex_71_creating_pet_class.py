import random

class Pet: # define a Pet class
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them
    """

# attributes of the class
    is_human = False
    owner = "Michael Smith"

# add additional parameter name
    def __init__(self, height, name=None):
        self.height = height
        self.name = name

# add additional special instance method
    def __str__(self):
        return '%s, height: %s cm' % (self.name, self.height)

# add additional instance 'is_tall' method
    def is_tall(self, tall_if_at_least):
        return self.height >= tall_if_at_least

# add static method. it doesn't use 'self'
    @staticmethod
    def owned_by_smith_family():
        return 'Smith' in Pet.owner

    @classmethod
    def create_random_heigh_pet(cls):
        height = random.randrange(1, 100)
        return cls(height)

# create an object of class
chubbles = Pet(height=5)
# check properties for chubbles
print(chubbles.is_human)
print(chubbles.owner)
print(chubbles.height)

# print docstring
print(chubbles.__doc__)

# create a new Pet
bowser = Pet(40)
print(bowser.is_tall(30))
bowser.height = 60
# print(bowser.is_tall()) #the instance method return TypeError as missing 1 required arguments
print(bowser.is_tall(bowser.height))
print(bowser.is_tall(70))

my_pet = Pet(30, 'Chis')
print(my_pet) # return address in memory instead of object's properties

# create another new pet
my_other_pet = Pet(40, 'Rudolf')
print(my_other_pet)

# test static method
nibbles = Pet(100)
print(nibbles.owned_by_smith_family())

# test @classmethod random assignee height
for i in range(5):
    pet = Pet.create_random_heigh_pet()
    print(pet.height)