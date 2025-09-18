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
squares = [x*x for x in range(-10, 11)]
print(f"3a: {squares}")
plt.plot(range(-10, 11), squares)
plt.title("3b: x^2")
plt.xlabel("Längd")
plt.ylabel("area")
plt.show()

#4
firstRow = [f"{x}1" for x in "ABCDEFGH"]
print(f"4a: {firstRow}")
chessBoard = [[f"{row}{column}" for row in "ABCDEFGH"] for column in range(1,9)] #note to self- good list comprehension
print(f"4b: {chessBoard}")

#5 Note to self- Matplotlib info
random.seed(1)
diceRollSix = 0
for i in range(100):
    if random.randint(1,6) == 6:
        diceRollSix += 1
print(f"5a: antal sexor rullade av 100: {diceRollSix}")
diceRollSix = 0
diceStatsX = []
diceStatsY = []
for i in range(1, 1000001):
    if random.randint(1,6) == 6:
        diceRollSix += 1
    if i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000 or i == 1000000:
        diceStatsX.append(i)
        diceStatsY.append(diceRollSix / i)
print(f"5b: {diceStatsY} sannorlikhet att få en sexa efter {diceStatsX} kast")
plt.plot(diceStatsY, "-*")
plt.title("5c: the probability of six for different numbers of rolls")
plt.xticks([0, 1, 2, 3, 4, 5], diceStatsX)
plt.xlabel("Number of dice rolls")
plt.ylabel("Probability")
plt.show()

#6
points = []
distance = []
red, blue = 0, 0
for i in range(5000):
    points.append([random.uniform(-1, 1), random.uniform(-1, 1)])
    distance.append(np.sqrt(np.pow(points[i][0], 2) + np.pow(points[i][1], 2)))
    if distance[i] > 1:
        points[i].insert(2, 'red')
        red += 1
    else:
        points[i].insert(2, 'blue')
        blue += 1
plt.scatter([x[0] for x in points], [y[1] for y in points], color = [c[2] for c in points], s = 10)
plt.axis('equal')
plt.show()
#Note to self- Fråga om convergence, hur tar jag reda på det?¨

#7
statistik = []
doorStatsX = []
switchStatsY = []
stayStatsY = []
for i in range(1, 1000001):
    kanin = random.randint(1,3)
    valdDörr = random.randint(1,3)
    statistik.append([kanin, valdDörr])
    if i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000 or i == 1000000:
        resultat = [1 for row in statistik if row[0] == row[1]]
        stayStatsY.append(resultat.count(1) / len(statistik))
        switchStatsY.append((len(statistik) - resultat.count(1)) / len(statistik))
        doorStatsX.append(i)
plt.plot(switchStatsY, "-*", label = "switch", color = "red")
plt.plot(stayStatsY, "-*", label = "stay", color = "blue")
plt.title("7b: probability of winning when switching vs not switching door")
plt.xticks([0, 1, 2, 3, 4, 5], diceStatsX)
plt.xlabel("Number simulations")
plt.ylabel("probability of winning")
plt.show()