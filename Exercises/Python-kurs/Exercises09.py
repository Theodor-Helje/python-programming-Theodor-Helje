import numpy as np
import matplotlib.pyplot as plt
import random
filePath = "File_Handling_And_Data"

#1
kurser = {
    'introduktionskurs': 5, 
    'programmering med python': 40, 
    'examensarbete': 15, 
    'djup maskininlärning': 40, 
    'data engineering och agila metoder': 45, 
    'databaser': 25, 
    'maskininlärning': 45, 
    'statistiska metoder': 30, 
    'linjär algebra': 20, 
    'databehandling': 25
}
poäng = sum([kurser[i] for i in kurser])
print(poäng)

#2
diceRolls = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0
}
for i in range(1000000):
    diceRolls[str(random.randint(1,6))] += 1
print(diceRolls)

#3
with open(rf"{filePath}\pokemon_list.txt", 'r') as data:
    pokemonList = data.read().splitlines()
pokemonList = [i.split() for i in pokemonList]

pokedex = {}
for i in pokemonList:
    pokedex[i[1]] = f"{i[2]}, {i[0]}"
print(pokedex)

#4
def morse(string):
    morseString = ''
    for i in string:
        morseString += morseDict[i]
    return(morseString)

with open(rf"{filePath}\morse.txt") as morseData:
    morseList = morseData.read().splitlines()
morseList = [i.split(': ') for i in morseList]

morseDict = {}
for i in morseList:
    morseDict[i[0]] = i[1]

print(f"morse: {morse(input("skriv något att översätta till morse: "))}")