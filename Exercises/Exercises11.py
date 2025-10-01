import numpy as np
import matplotlib.pyplot as plt

#1
class UnitUs: #följer alla konventioner och felfri syntax
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The value must be int or float")
        elif value <= 0:
            raise ValueError("The value must be > 0")
        self._value = value

    def inch_to_cm(self):
        return(self.value * 2.54)

    def foot_to_meters(self):
        return(self.value * 0.3048)

    def pound_to_kg(self):
        return(self.value * 0.45359237)

    def __repr__(self):
        return f"UnitUs(value='{self.value}')"

units = UnitUs(1)
for i in range(1, 11):
    units.value = i
    print(f"{units.value} inches is {units.inch_to_cm()} centimeters")
    print(f"{units.value} feet is {units.foot_to_meters()} meters")
    print(f"{units.value} pounds is {units.pound_to_kg()} kilograms")

#2