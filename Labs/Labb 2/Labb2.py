#This project uses the enviroment "exercises_env"
import numpy as np
import matplotlib.pyplot as plt
import random
filePath = "Labs\Labb 2\Data_And_Testdata"
k = 1

def getUserPositiveNumericInput(firstMessage):
    while True:
        try:
            number = input(f"{firstMessage} ")
            number = float(number)
            if number <= 0:
                print(f"{number} är inte ett positivt nummer, skriv in ett nummer")
            else:
                break
        except ValueError:
            print(f"{number} är inte ett positivt nummer, skriv in ett nummer igen")
    return(number)


def knnClassification(k, dataList, dataTest):
    pichu, pikachu = 0, 0
    distanceList = [[np.sqrt(np.pow(dataTest[0] - i[0], 2) + np.pow(dataTest[1] - i[1], 2)), i[2]] for i in dataList]
    distanceList.sort(key = lambda distanceKey : distanceKey[0])
    for i in range(k):
        if distanceList[i][1] == 0:
            pichu += 1
        else:
            pikachu +=1
    if pichu > pikachu:
        pokemon = "Pichu"
        #prediction[pokemon] = "Pichu"
    else:
        pokemon = "Pikachu"
    return(pokemon)

with open(rf"{filePath}\datapoints.txt",'r') as dataFile:
    dataList = dataFile.read().splitlines()
dataList.pop(0)
dataPoints = [i.split(', ') for i in dataList]
dataPoints = [[float(i[0]), float(i[1]), int(i[2])] for i in dataPoints]
pichuDataPoints = [i for i in dataPoints if i[2] == 0]
pikachuDataPoints = [i for i in dataPoints if i[2] == 1]

userPoints = [getUserPositiveNumericInput("1: input width:"), getUserPositiveNumericInput("1: input height:")]

plt.scatter([x[0] for x in pichuDataPoints], [y[1] for y in pichuDataPoints], c = 'red', label = "Pichu")
plt.scatter([x[0] for x in pikachuDataPoints], [y[1] for y in pikachuDataPoints], c = 'orange', label = "Pikachu")
plt.scatter(userPoints[0], userPoints[1], c = 'blue', label = f"predicted (k = {k}): {knnClassification(k, dataPoints, userPoints)}")
plt.scatter(userPoints[0], userPoints[1], c = 'blue', label = f"predicted (k = {k*10}): {knnClassification(k*10, dataPoints, userPoints)}")
plt.xlabel("width")
plt.ylabel("height")
plt.title(f"uppgift 1 och 2:")
plt.legend()
plt.show()

testData = []
trainingData = []
testReslutData = 0
random.shuffle(pichuDataPoints)
random.shuffle(pikachuDataPoints)

for i in range(75): #because our data set never changes
    if i < 25:
        testData.append([pichuDataPoints[i], 'Pichu'])
        testData.append([pikachuDataPoints[i], 'Pikachu'])
    else:
        trainingData.append(pichuDataPoints[i])
        trainingData.append(pikachuDataPoints[i])

for i in range(50):
    testReslutData += 1 if knnClassification(k, trainingData, testData[i][0]) == testData[i][1] else 0
print(f"{testReslutData/len(testData)}")