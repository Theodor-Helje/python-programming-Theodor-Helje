import math
#1
nummer = int(input("1: skriv ett nummer "))
if nummer < 0:
    print (f"1: numret är negativt")
elif nummer > 0:
    print (f"1: numret är positivt")
else:
    print (f"1: numret är 0")

#2
nummer1 = int(input("2: skriv ett nummer "))
nummer2 = int(input("2: skriv ett till nummer "))
if nummer1 < nummer2 and not nummer1 == nummer2:
    print(f"2: {nummer1} är minst")
elif not nummer1 == nummer2:
    print(f"2: {nummer2} är minst")
else:
    print("2: båda är lika stora")

#3
vinkel1, vinkel2, vinkel3 = 0, 0, 0
while not vinkel1 + vinkel2 + vinkel3 == 180:
    vinkel1 = int(input("3: skriv första vinkeln på triangeln "))
    vinkel2 = int(input("3: skriv andra vinkeln på triangeln "))
    vinkel3 = int(input("3: skriv tredje vinkeln på triangeln "))
    if not vinkel1 + vinkel2 + vinkel3 == 180:
        print("3: vinklarna kan inte skapa en triangel")
if vinkel1 == 90 or vinkel2 == 90 or vinkel3 == 90:
    print("3: det är en rätvinklig triangel")
else:
    print("3: triangeln är inte rätvinklig")

#4
ålder = int(input("4: skrin in ålder "))
vikt = int(input("4: skriv in vikt "))
if 3 <= ålder <= 12:
    if 15 <= vikt <= 25:
        print("4: 1/2 piller")
    elif 25 <= vikt <= 40:
        print("4: 1/2 - 1 piller")
    elif vikt > 40:
            print("4: 1-2 piller")
    else:
        print("4: 0 piller")
elif ålder >= 12:
    print("4: 1-2 pills")

#5
nummer = int(input("5: skriv ett nummer "))
if nummer % 2 == 0:
    print(f"5: {nummer} är jämt")
else:
    print(f"5: {nummer} är ojämt")
if nummer % 5 == 0:
    print(f"5: {nummer} är delbart med 5")
else:
    print(f"5: {nummer} är inte delbart med 5")
if nummer % 5 == 0 and nummer % 2 != 0:
    print(f"5: {nummer} är både delbart med 5 och ojämt")

#6
vikt = int(input("6: skriv in vikt för ditt bagage "))
längd  = int(input("6: skriv in längd för ditt bagage "))
bredd = int(input("6: skriv in bredd för ditt bagage "))
höjd = int(input("6: skriv in höjd för ditt bagage "))
if vikt <= 8 and längd <= 55 and bredd <= 40 and höjd <= 23:
    print("ditt bagage är godkänt")
else:
    print("ditt bagage är inte godkänt")