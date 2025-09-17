import numpy as np
import matplotlib.pyplot as plt
import random
#1
diceRolls = []
for i in range(10):
    diceRolls.append(random.randint(0,6))
diceRolls.sort()
print(f"1a: ascending order: {sorted(diceRolls)}")
print(f"1b: descending order: {sorted(diceRolls, reverse = True)}")
print(f"1c: Maximum: {diceRolls[-1]}, Minimum: {diceRolls[0]}")

#2
mat = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
veckodagar = ["mån", "tis", "ons", "tors", "fre"]
for dag, mat in zip(veckodagar, mat):
    print(f"2: {dag}: {mat}")

#3
lines = []
for i in range(-10, 11):
    lines.append(i)
squares = [x*x for x in lines]
print(f"3a: {squares}")
plt.plot(lines, squares)
plt.title("3b: x^2")
plt.xlabel("Längd")
plt.ylabel("area")
plt.show()

#4
