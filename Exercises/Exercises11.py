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

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def email(self):
        return self._email
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    @age.setter
    def age(self, age):
        if not isinstance(age, (int, float)):
            raise TypeError("age must be int or float")
        elif not 0 <= age <= 125:
            raise ValueError("age must be 0 <= age <= 125")
        self._age = age

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("email must be a string")
        elif not '@' in email:
            raise NameError("email must contain @")
        self._email = email
    
    def say_hello(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, my email adress is {self.email}")
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"

p = Person("Theodor", 20, "Theodor.Helje@iths.se")
print(p)
p.say_hello()

#3
class Student(Person):
    def study(self):
        print("study...study...study...more study")
    def say_hello(self):
        print(f"Yo, I am a student, my name is {self.name}, I am {self.age} years old, my email adress is {self.email}")
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, email={self.email})"
    
class Teacher(Person):
    def teach(self):
        print("teach...teach...teach...mroe teaching")

t = Teacher("Pernilla", 32, "pernilla@gmail.com")
s = Student("Karl", 25, "karl@gmail.com")
t.teach()
t.say_hello()
s.study()
s.say_hello()