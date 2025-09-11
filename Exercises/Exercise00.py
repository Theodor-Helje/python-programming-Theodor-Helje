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