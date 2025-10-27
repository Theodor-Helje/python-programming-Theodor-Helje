import numpy as np
import matplotlib.pyplot as plt
import random
import string

#1
ord  = str(input("skriv ett ord: "))
bokstäver, storaBokstäver, småBokstäver = 0, 0, 0
for i in ord:
    bokstäver += 1
    if i.isupper():
        storaBokstäver += 1
    elif i.islower():
        småBokstäver += 1
print(f"1: {ord} består av {bokstäver} bokstäver, varav {storaBokstäver} är stora och {småBokstäver} är små.")

#2
mening = "A picture says more than a thousand words, a mathematical formula says more than a thousand pictures."
print(f"2: {mening} består av {len(mening.split())} ord.")

#3
palindrome = str(input("skriv ett ord för att se om det är ett palindrom: "))
cleanPalindrome = palindrome.translate(str.maketrans('', '', f"{string.whitespace}{string.punctuation}"))
omvänt = cleanPalindrome[::-1]
print(omvänt)
if omvänt == palindrome:
    print(f"3: {palindrome } är ett palindrom")
else:
    print(f"3: {palindrome} är inte ett palindrom")

#4
antalVokaler = 0
vokaler = 'aeiouyåäö'
mening = "Pure mathematics is, in its way, the poetry of logical ideas"
utanVokaler = mening.lower().translate(str.maketrans('', '', vokaler + string.whitespace))
medVokaler = mening.lower().translate(str.maketrans('', '', string.whitespace))
for i in medVokaler:
    antalVokaler += 1
for i in utanVokaler:
    antalVokaler -= 1
print(f"4: {mening} innehåller {antalVokaler} vokaler")

#5
encrypt = str.maketrans('ö' + string.ascii_letters + 'åä', string.ascii_letters + 'åäö')
decrypt = str.maketrans( string.ascii_letters + 'åäö', 'ö' + string.ascii_letters + 'åä')
ord = str(input("5: skriv ett ord som ska krypteras: "))
ord = ord.translate(encrypt)
print(f"5a: krypterat: {ord}")
ord = ord.translate(decrypt)
print(f"5b: avkrypterat: {ord}")
while(True):
    val = str(input("tryck enter för att kryptera ett meddelande eller skriv något för att avkryptera"))
    if val == '':
        ord = str(input("Vad vill du kryptera? ")).translate(encrypt)
        print(f"krypterat: {ord}")
    else:
        ord = str(input("Vad vill du avkryptera? ")).translate(decrypt)
        print(f"avkrypterat: {ord}")