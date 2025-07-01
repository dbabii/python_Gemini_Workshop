class Pet: # define a Pet class
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them
    """
    # attributes of the class
    is_human = False
    owner = "Michael Smith"


# create an object of class
chubbles = Pet()
# check properties for chubbles
print(chubbles.is_human)
print(chubbles.owner)
# print docstring
print(chubbles.__doc__)
