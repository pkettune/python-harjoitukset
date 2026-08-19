import random

dice = 0

sideInput = int(input("How many sides in the die? "))

def throw(sideCount):
    sideCount = sideInput
    return random.randint(1,sideCount)

while (dice <= sideInput):
    dice = throw(sideInput)
    if(dice < sideInput):
        print(dice)
    else:
        print(dice)
        break