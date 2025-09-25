import numpy as np
import matplotlib.pyplot as plt
import random

#1
theoreticalMean = np.sum(range(1,7)) / 6
print(theoreticalMean)

diceRollValues = np.array(np.random.randint(1,6, size = 1000000))
#Skapa np.array
#np.mean på arrayen
print(diceRollValues)