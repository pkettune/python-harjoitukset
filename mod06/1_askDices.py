import random

askedDice = int(input("How many dices you want to roll? "))

dices = []

i = 0
while i < askedDice:
    dices.append(askedDice)
    i = i + 1

for i in dices:
    print (random.randint(1, 6))