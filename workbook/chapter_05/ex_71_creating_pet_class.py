class Pet: # define a Pet class
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them
    """
    def __init__(self, height):
        self.height = height

    # attributes of the class
    is_human = False
    owner = "Michael Smith"
    # add additional instance 'is_tall' method
    def is_tall(self):
        return self.height >= 50


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
print(bowser.is_tall())
bowser.height = 60
print(bowser.is_tall())