import random

dice = 0

def throw():
    return random.randint(1,6)

while (dice <= 6):
    dice = throw()
    if(dice < 6):
        print(dice)
    else:
        print(dice)
        break