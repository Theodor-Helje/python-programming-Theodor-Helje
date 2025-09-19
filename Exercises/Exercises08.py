import numpy as np
import matplotlib.pyplot as plt
import random
import os
filePath = "File_Handling_And_Data"

simulatedRolls = [random.randint(1,6) for i in range(20)]
with open(rf"{filePath}\dice_rolls.txt",'w') as diceRolls:
    diceRolls.write("Simulated 20 dice rolls:\n")
    diceRolls.write(f"{simulatedRolls}\n")
    diceRolls.write("\n")
    diceRolls.write("Sorted dice rolls:\n")
    diceRolls.write(f"{sorted(simulatedRolls)}\n")
    diceRolls.write("\n")
    diceRolls.write(f"Number of fours: {simulatedRolls.count(4)}\n")
print(f"1: Done.")

#2
with open(rf"{filePath}\test_result.txt", 'r') as data:
    testData = data.read()

dataList = testData.splitlines()
dataList.sort()

def getGrade(grade):
    grade = int(grade)
    if grade < 20:
        gradeText = "Grade: F"
    elif grade < 30:
        gradeText = "Grade: E"
    elif grade < 40:
        gradeText = "Grade: D"
    elif grade < 50:
        gradeText = "Grade: C"
    elif grade < 60:
        gradeText = "Grade: B"
    else:
        gradeText = "Grade: A"
    return(gradeText)

scoreSorted = [i.split() for i in dataList]
scoreSorted.sort(key = lambda element : element[-1])
#[print(f"{getGrade(words[-1])}\n{" ".join(words)}\n") for words in scoreSorted]

with open(rf"{filePath}\text_result_copy.txt", 'w') as dataCopy:
    dataCopy.write(testData)
    dataCopy.write("\n \n")
    dataCopy.write("Sorted alphabetically:\n")
    [dataCopy.write(f"{i}\n") for i in dataList]
    dataCopy.write("\n")
    dataCopy.write("Sorted by grade:\n\n")
    [dataCopy.write(f"{getGrade(words[-1])}\n{" ".join(words)}\n\n") for words in scoreSorted]
print(f"2 and 3: Done.\n\n")

diceRollsPath = os.path.abspath(rf"{filePath}\dice_rolls.txt")
textResultCopyPath = os.path.abspath(rf"{filePath}\text_result_copy.txt")
if input("tryck enter för att behålla filerna, skriv vad som helst för att ta bort dem.") != '':
    os.remove(diceRollsPath)
    os.remove(textResultCopyPath)
    print(f"{diceRollsPath} deleted")
    print(f"{textResultCopyPath} deleted")
print("done.")