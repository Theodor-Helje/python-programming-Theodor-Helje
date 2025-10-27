#This project uses the enviroment "exercises_env"
import numpy as np
import matplotlib.pyplot as plt
import random
filePath = "Labb 2\Data_And_Testdata"
k = 1
timesToSimulateAccuracy = 10

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
    prediction = {}
    pichu, pikachu = 0, 0
    distanceList = [[np.sqrt(np.pow(dataTest[0] - i[0], 2) + np.pow(dataTest[1] - i[1], 2)), i[2]] for i in dataList]
    distanceList.sort(key = lambda distanceKey : distanceKey[0])
    for i in range(k):
        if distanceList[i][1] == 0:
            pichu += 1
        else:
            pikachu +=1
    if pichu > pikachu:
        prediction ['pokemon'] = "Pichu"
        prediction ['pokemonClass'] = 0
    else:
        prediction ['pokemon'] = "Pikachu"
        prediction ['pokemonClass'] = 1
    return(prediction)

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
plt.scatter(userPoints[0], userPoints[1], c = 'blue', label = f"predicted (k = {k}): {knnClassification(k, dataPoints, userPoints)['pokemon']}")
plt.scatter(userPoints[0], userPoints[1], c = 'blue', label = f"predicted (k = {k*10}): {knnClassification(k*10, dataPoints, userPoints)['pokemon']}")
plt.xlabel("width")
plt.ylabel("height")
plt.title(f"uppgift 1 och 2:")
plt.legend()
plt.show()

accuracy = []
for i in range(timesToSimulateAccuracy):
    testData = []
    trainingData = []
    testReslutData = 0
    random.shuffle(pichuDataPoints)
    random.shuffle(pikachuDataPoints)

    for j in range(75):
        if j < 25:
            testData.append(pichuDataPoints[j])
            testData.append(pikachuDataPoints[j])
        else:
            trainingData.append(pichuDataPoints[j])
            trainingData.append(pikachuDataPoints[j])

    for j in range(50):
        testReslutData += 1 if knnClassification(k, trainingData, testData[j])['pokemonClass'] == testData[j][2] else 0

    accuracy.append(testReslutData/len(testData))

plt.plot(range(1,timesToSimulateAccuracy + 1), accuracy, marker = 'o', color = 'blue', label = "accuracy of simulation x")
plt.xticks(range(1,timesToSimulateAccuracy + 1))
plt.title(f"average accuracy: {sum(accuracy) / len(accuracy):.3f}")
plt.xlabel("times simulated")
plt.ylabel("accuracy")
plt.grid()
plt.show()