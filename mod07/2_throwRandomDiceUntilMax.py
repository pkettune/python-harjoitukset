import random

dice = 0

sides = int(input("How many sides in the die? "))

def throw(side):
    side = sides
    return random.randint(1,side)

while (dice <= sides):
    dice = throw(sides)
    if(dice < sides):
        print(dice)
    else:
        print(dice)
        break