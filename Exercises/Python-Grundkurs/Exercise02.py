import numpy as np
import random
#1
i = -10
while i <= 10:
    print(f"1: {i} ")
    i += 1

#2
sumAll, sumOdd = 0, 0
i = 1
while i <= 100:
    sumAll += i
    if i % 2 == 1:
        sumOdd += i
    i += 1
print (f"2: summan av talen 1 till 100 är {sumAll}")
print (f"2: summan av de udda talen 1-100 är {sumOdd}")

#3
randomInt = random.randint(1,100)
guesses = 1
userGuess = int(input("3a: gissa vilket tal mellan 1 och 100 som är rätt: "))
computerGuesses = 1
computerGuess = 50
computerGuess
computerGuessIncrement = 25
while userGuess !=  randomInt:
    if randomInt < userGuess and userGuess != randomInt:
        userGuess = int(input("3a: Fel! Talet är lägre än så! Gissa igen: "))
    elif randomInt > userGuess and userGuess != randomInt:
        userGuess = int(input(f"3a: Fel! Talet är högre än så! Gissa igen: "))
    guesses += 1
    if computerGuess < randomInt:
        computerGuess += computerGuessIncrement
        computerGuesses += 1
    elif computerGuess > randomInt:
        computerGuess -=  computerGuessIncrement
        computerGuesses += 1
    if computerGuessIncrement > 1:
        computerGuessIncrement = computerGuessIncrement // 2
print(f"3a: Grattis, Du gissade rätt på försök {guesses}. Talet var {randomInt}")
print(f"3b: Datorn gissade på {computerGuess} efter {computerGuesses} försök")

#4
score = 0
while True:
    multiplicationFactor = int(input("4: select max multiplication factor: "))
    randomX, randomY = random.randint(1,multiplicationFactor), random.randint(1,multiplicationFactor)
    guess = int(input(f"4: vad blir {randomX} * {randomY}? "))
    if guess == randomX * randomY:
        score += 1
        print(f"4: Du gissade rätt, ditt score är nu {score}!")
    else:
        print(f"4: Du gissade fel, rätt svar vad {randomX * randomY}! Ditt score förblir {score}")
    if not input("4: Vill du fortsätta spela? (ja/nej): ").strip().lower() == "ja":
        break
print(f"4: Tack för att du spelade, du fick {score} poäng")

#5
sumA, sumB = 0, 0
#i = 1
n = int(input("5: Hur många gånger ska programmet loopa för att få fram summorna? "))
for i in range(n):
    sumA += 1 / np.pow(2.0, i)
    sumB += np.pow(-1, i) / (2 * i + 1)
    #i += 1
print(f"5: Summa A blev {sumA} och summa B blev {sumB}")