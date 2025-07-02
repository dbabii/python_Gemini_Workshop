class Pet: # define a Pet class
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them
    """
# add additional parameter name
    def __init__(self, height, name=None):
        self.height = height
        self.name = name


    # attributes of the class
    is_human = False
    owner = "Michael Smith"
    # add additional instance 'is_tall' method
    def is_tall(self, tall_if_at_least):
        return self.height >= tall_if_at_least


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