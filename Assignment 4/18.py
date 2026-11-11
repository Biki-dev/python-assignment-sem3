class Temperature:
    def __init__(self, kelvin):
        if kelvin < 0:
            raise ValueError("Temperature cannot be below absolute zero")
        self._kelvin = kelvin
    @property
    def celsius(self):
        return self._kelvin - 273.15
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15 Celsius")
        self._kelvin = value + 273.15
    @celsius.deleter
    def celsius(self):
        del self._kelvin
    @property
    def fahrenheit(self):
        return self._kelvin * 9 / 5 - 459.67
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -459.67:
            raise ValueError("Temperature cannot be below -459.67 Fahrenheit")
        self._kelvin = (value + 459.67) * 5 / 9
    @fahrenheit.deleter
    def fahrenheit(self):
        del self._kelvin
temp = Temperature(300)
print("Temperature in Kelvin:", temp._kelvin)
print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", temp.fahrenheit)
temp.celsius = 25
print("\nAfter setting Celsius:")
print("Kelvin:", temp._kelvin)
print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit)
temp.fahrenheit = 98.6
print("\nAfter setting Fahrenheit:")
print("Kelvin:", temp._kelvin)
print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit)
try:
    temp.celsius = -300
except ValueError as e:
    print("\nError:", e)
del temp.celsius
temp2 = Temperature(300)
del temp2.fahrenheit