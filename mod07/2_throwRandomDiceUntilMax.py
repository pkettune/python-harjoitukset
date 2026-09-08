import random

dice = 0

sideInput = int(input("How many sides in the die? "))

def throw(sideCount):
    return random.randint(1,sideCount)

while (dice != sideInput):
    dice = throw(sideInput)
    print(dice)