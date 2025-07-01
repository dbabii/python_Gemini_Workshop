class Circle:
    # any object of the class will have this attribute
    is_shape = True
    # add __init__ method with instance attributes. They can be different for each objects
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

# creating objects with different attributes
first_circle = Circle(2, 'blue')
second_circle = Circle(3, 'red')

print(first_circle.is_shape)
print(first_circle.radius)
print(first_circle.color)

print(second_circle.is_shape)
print(second_circle.radius)
print(second_circle.color)