import numpy as np
import matplotlib.pyplot as plt
import random

#1
def distance(x,y):
    return np.sqrt(np.pow(x, 2) + np.pow(y, 2))

print(distance(0.5, 0.5))

#2

def is_fourdigit(number):
    if 1 <= np.abs(number)//1000 < 10:
        return True
    else:
        return False

# test program
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")

#3

while True:
    try:
        antalSpårvagn = int(input("Hur många gånger tar du spårvagnen per månad? "))
        if 0 <= antalSpårvagn <= 100:
            break
        print(f"Det är helt orimligt att du åker spårvagn {antalSpårvagn} gånger i månaden, skriv in ett rimligt nummer. (0-100)")
    except ValueError:
        print(f"Du skrev inte in ett heltal, försök igen!")
while True:
    try:
        enkelBiljettKostnad = int(input("Hur mycket kostar en enkelbiljett? (kr) "))
        if 0 <= enkelBiljettKostnad <= 100:
            break
        print(f"En enkenbiljett kan omöjligt kosta {enkelBiljettKostnad} kr, försök igen. (0-100 kr)")
    except ValueError:
        print(f"Du skrev inte in ett heltal, försök igen!")
while True:
    try:
        månadsBiljettKostnad = int(input("Hur mycket kostar Ett månadskort? (kr) "))
        if 0 <= månadsBiljettKostnad <= 1500:
            break
        print(f"Ett månadskort kan omöjligt kosta {månadsBiljettKostnad} kr, försök igen. (0-1500)")
    except ValueError:
        print(f"Du skrev inte in ett heltal, försök igen!")
print(f"kostnad om du köper enkelbiljettet: {enkelBiljettKostnad * antalSpårvagn}")
print(f"kostnad om du köper månadskort: {månadsBiljettKostnad}")
if månadsBiljettKostnad <= enkelBiljettKostnad:
    print(f"Det är mest värt att köpa månadskort.")
else:
    print(f"Det är mest värt att köpa enkelbiljetter.")