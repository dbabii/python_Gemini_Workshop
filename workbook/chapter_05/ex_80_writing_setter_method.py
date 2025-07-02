class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32
# convert fahrenheits to celsius
    @fahrenheit.setter
    def fahrenheit(self, value):
# added validation of value
        if value <= -460:
            raise ValueError('Temperature less than -460F are not possible')
        self.celsius = (value - 32) * 5 / 9

temp = Temperature(5)
print(temp.fahrenheit)
temp.fahrenheit = 32
print(temp.celsius)

temp.fahrenheit = -460
print(temp.fahrenheit)