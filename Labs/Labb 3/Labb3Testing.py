import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
filePath = r"C:\Users\herrt\Desktop\Git Repos\python-programming-Theodor-Helje\Labs\Labb 3"
line = "y = -x"

def classifyPoint(k, m, xPoint, yPoint):
    yLine = k * xPoint + m
    if yPoint < yLine:
        classification = 'red' #0
    else:
        classification = 'blue' #1
    return(classification)

dataPoints = pd.read_csv(rf"{filePath}\unlabelled_data.csv", header = None)
dataPoints[2] = dataPoints.apply(lambda row : classifyPoint(-1, 0, row[0], row[1]), axis = 1)

plt.scatter(dataPoints[0], dataPoints[1], color = dataPoints[2])
x = [-5, 5]
y = [5, -5]
plt.plot(x, y, color = 'black')
plt.show()