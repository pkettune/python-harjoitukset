import random

askedDice = int(input("How many dices you want to roll? "))

dices = []

sum = 0

i = 0
while i < askedDice:
    dice = random.randint(1, 6)
    dices.append(dice)
    i = i + 1

for d in dices:
    sum = sum + d
    print (dices)

print (sum)