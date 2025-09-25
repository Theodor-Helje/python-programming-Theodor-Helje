import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
filePath = r"C:\Users\herrt\Desktop\Git Repos\python-programming-Theodor-Helje\Labs\Labb 3"

def classifyPoint(k, m, xPoint, yPoint):
    yLine = k * xPoint + m
    if yPoint < yLine:
        classification = 0
    else:
        classification = 1
    return(classification)

dataPoints = pd.read_csv(rf"{filePath}\unlabelled_data.csv", header = None)
dataPoints[2] = dataPoints.apply(lambda row : classifyPoint(-1, 0, row[0], row[1]), axis = 1)

with open(rf"{filePath}\labelled_data.csv", 'w', newline="") as labelledData:
    labelledData.write(dataPoints.to_csv(index=False, header=False))
print("Writing labelled_data.csv complete.")

plt.scatter(dataPoints[0], dataPoints[1], color = ['blue' if i == 1 else 'red' for i in dataPoints[2]])
plt.plot([-5, 5], [5, -5], color = 'black')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()