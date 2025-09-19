import numpy as np
import matplotlib.pyplot as plt
import random

#1
def area(base, height):
    return((base * height) / 2)

bas = 3
höjd = 2
#bas = int(input("skriv in basen på triangeln: "))
#höjd = int(input("skriv in höjden på triangeln: "))
print(f"1: en triangel med basen {bas} och höjden {höjd} har arean {area(bas, höjd)}")

#2
def EucDistance(p1, p2, q1, q2):
    return(float(round(np.sqrt(np.pow(p1 - q1, 2) + np.pow(p2 - q2, 2)), 1)))

#p1 = int(input("2: skriv in första punkten X: "))
#p2 = int(input("2: skriv in första punkten Y: "))
#q1 = int(input("2: skriv in andra punkten X: "))
#q2 = int(input("2: skriv in andra punkten Y: "))
p1, p2, q1, q2 = 1, 2, 3, 4
print(f"anståndet mellan {p1}:{p2} och {q1}:{q2} är {EucDistance(p1,p2,q1,q2)}")
points = [[10,3],[-1,-9],[10,-10],[4,-2],[9,-10]]
distances = [EucDistance(row[0], row[1], 0, 0) for row in points]
print(f"2: anståndet mellan {points} och 0:0 är {distances}")

#3
fx = lambda x : np.pow(x,2) - 3
gx = lambda x : 4 * x - 7
fxPlot = fx(np.linspace(-10, 10))
gxPlot = gx(np.linspace(-10, 10))
plt.plot(np.linspace(-10,10), fxPlot)
plt.plot(np.linspace(-10,10), gxPlot)
plt.show()
print(f"3: g(x) är derivatan av f(x)")

#4
def nameCleaner(uncleanedName):
    cleanedName = ''
    uncleanedName = uncleanedName.lower()
    nameList = uncleanedName.split()
    for name in nameList:
        print(name.title()) #felsökning
        cleanedName += f"{name.title()} "
    cleanedName = cleanedName.strip()
    return(cleanedName)

names = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]
cleanedNames = [nameCleaner(name) for name in names]
print(f"4: {cleanedNames}")

#5
def changeFunction(money):
    tusen = f"{money // 1000} tusenlappar"
    money %= 1000
    femhundra = f"{money // 500} femhundralappar"
    money %= 500
    tvåhundra = f"{money // 200} tvåhundralappar"
    money %= 200
    hundra = f"{money // 100} hundralappar"
    money %= 100
    femtio = f"{money // 50} femtiolappar"
    money %= 50
    tjugo = f"{money // 20} tjugolappar"
    money %= 20
    tio = f"{money // 10} tior"
    money %= 10
    fem = f"{money // 5} femmor"
    money %= 5
    två = f"{money // 2} tvåor"
    money %= 2
    ett = f"{money // 1} ettor"
    changelist = [tusen, femhundra, tvåhundra, hundra, femtio, tjugo, tio, fem, två, ett, f"{(money * 100):.0f} öre blir över"]
    return(changelist)

#change = str(input("hur mycket vill du växla? "))
change = 5289
changelist = changeFunction(change)
print(f"växel för {change}")
for i in changelist:
    print(i)