import numpy as np
import matplotlib.pyplot as plt

#1
class unitUs:
    def __init__(self, value):
        self.value = value
    def inch_to_cm(self):
        return(self.value * 25.4)
    def foor_to_meters(self):
        return(self.value * 0.3048)
    def pound_to_kg(self):
        return(self.value * 0.45359237)
    def __repr__(self):
        pass