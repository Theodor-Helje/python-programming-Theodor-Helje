import numpy as np
import matplotlib.pyplot as plt
import random

#1
theoreticalMean = np.sum(range(1,7)) / 6
print(theoreticalMean)
meanValues = []
for i in range(1, 1000001):
    if i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000 or i == 1000000:
        diceRollValues = np.array(np.random.randint(1,6, size = i))
        meanValues.append(float(np.mean(diceRollValues)))
print(meanValues)

#2
diceOutcomesX, diceOutcomesY = np.meshgrid(range(1,7), range(1, 7))
diceGrid = diceOutcomesX + diceOutcomesY
for i in range(2,13):
    print(f"{i} accurs {np.count_nonzero(diceGrid == i)} times, frequency: {np.count_nonzero(diceGrid == i) / np.count_nonzero(diceGrid)}")
frequency = [np.count_nonzero(diceGrid == i) / np.count_nonzero(diceGrid) for i in range(2, 13)]

plt.subplot(2, 2, 1)
plt.bar(range(1, 7), [1/6 for _ in range(6)])
plt.title("1 dice probability distribution")

plt.subplot(2, 2, 2)
plt.bar(range(2, 13), frequency)
plt.title("2 dices probability distributions")

plt.subplot(2, 2, 3)
diceOutcomesX, diceOutcomesY, diceOutcomesZ = np.meshgrid(range(1,7), range(1,7), range(1,7))
diceGrid = diceOutcomesX + diceOutcomesY + diceOutcomesZ
plt.bar(range(3, 19), [np.count_nonzero(diceGrid == i) / np.count_nonzero(diceGrid) for i in range(3, 19)])
plt.title("3 dices probability distributions")

plt.subplot(2, 2, 4)
diceOutcomesX, diceOutcomesY, diceOutcomesZ, diceOutcomesFour = np.meshgrid(range(1,7), range(1,7), range(1,7), range(1,7))
diceGrid = diceOutcomesX + diceOutcomesY + diceOutcomesZ + diceOutcomesFour
plt.bar(range(4, 25), [np.count_nonzero(diceGrid == i) / np.count_nonzero(diceGrid) for i in range(4, 25)])
plt.title("4 dices probability distributions")
plt.show()