import numpy as np
import random
#1
for i in range(-10, 11):
    print(i)
for i in range(-10,11,2):
    print(i)

#2
sumA, sumB = 0, 0
for i in range(101):
    sumA += i
for i in range(1,101,2):
    sumB += i
print(f"2a: summan blev {sumA}")
print(f"2b: summan blev {sumB}")

#3
row = ""
for i in range(11):
    row += str(f"{6 * i} ")
print(f"3a: {row}")
table = int(input("3b: Vilken multiplikationstabell vill du se? "))
start = int(input("3b: Defniera starten av tabellen: "))
slut = int(input("3b: definiera slutet på tabellen: "))
row = ""
for i in range(start, slut + 1):
    row += str(f"{table * i} ")
print(f"3b: multiplikationstabellen: {table} från {start} to {slut}: {row}")
for i in range(11):
    row = ""
    for j in range(11):
        row += str(f"{i * j} ")
    print(f"3c: {row}")

#4
n = int(input("4: välj ett tal att räkna ut n!1 för: "))
faculty = 1
for i in range(1, n + 1):
    faculty *= i
print(f"4: svar: {faculty}")

#5
numberGuess = 0
number = random.randrange(0,9999)
for i in range(10000): #riktigt lat lösning
    if i == number:
        numberGuess = i
print(f"5: numret var: {number}")
print(f"5: numret datorn gissade på var: {numberGuess}")

#6
rice = 0
for i in range (64):
    rice += np.pow(2.0, i)
print(f"6: there are {rice} grains of rice on the chessboard")