import math
#onödiga variabler för att "remember to use variables"
#1A
cathetusA = 3
cathetusB = 4
hypothenuse = math.sqrt(cathetusA ** 2 + cathetusB ** 2)
print (f"1A: the hypothenuse is {hypothenuse}")

#1b
hypothenuse = 7
cathetusA = 5
cathetusB = math.sqrt(hypothenuse ** 2 - cathetusA ** 2)
print (f"1B: The unknown cathetus is {round(cathetusB, 1)}")

#2
correctML = 300
totalML = 365
accuracyML = round((300/365), 3)
print(f"2: the accuracy is {accuracyML} or {round(accuracyML*100, 1)}%")

#3
TP = 2
FP = 2
FN = 11
TN = 985
accuracy = round((TP + TN)/(TP+TN+FP+FN), 3)
print (f"3: the model has an accuracy of {accuracy} or {round(accuracy * 100, 1)}")
print(f"given the {FN} false negatives, this is not a good model.")

#4
AX = 4
AY = 4
BX = 0
BY = 1
k = (BY - AY) / (BX - AX)
m = AY - (k * AX)
print (f"4: the equation of the slope is y = {k}x + {m}")

#5
p1X = 3
p1Y = 5
p2X = -2
p2Y = 4
distance = math.sqrt((p2X - p1X) ** 2 + (p2Y - p1Y) ** 2)
print (f"5: the distance in 2D between p1 and p2 is {round(distance, 1)} units")

#6
p1X = 2
p1Y = 1
p1Z = 4
p2X = 3
p2Y = 1
p2Z = 0
distance = math.sqrt((p2X - p1X) ** 2 + (p2Y - p1Y) ** 2 + (p2Z - p1Z) ** 2)
print (f"6: the distance in 3D between p1 and p2 is {round(distance, 2)} units")