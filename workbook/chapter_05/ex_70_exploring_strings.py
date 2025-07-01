my_str = 'hello World!'
print(type(my_str))

print(my_str.__doc__) # print docsting for 'my_str' object
print(my_str.__dir__()) # print full list of properties and methods

# print each of property in separate string
# for i in my_str.__dir__():
#     print(i)

print(my_str.capitalize()) # First letter is capitalized, all other will be in lowercase
print(my_str.upper()) # all letters are capitalized
print(my_str.replace(" ",'_')) # replace space between words to underscore

print(my_str) # methods don't change the origin of object

