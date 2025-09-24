import numpy as np
import matplotlib.pyplot as plt
import random

#1
theoreticalMean = np.sum(range(1,7)) / 6
print(theoreticalMean)

diceRollValues = 0
for i in range(1,1000001):
    diceRollValues += random.randint(1,6)
    if i == 10^