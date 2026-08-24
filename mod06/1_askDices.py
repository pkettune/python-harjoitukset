import random

askedDice = int(input("How many dices you want to roll? "))
dices = [0 for _ in range(askedDice)]
#https://stackoverflow.com/questions/10712002/create-an-empty-list-with-certain-size-in-python
#you can do this: a = [0 for _ in range(10)]

sum = 0
for d in dices:
    sum = sum + random.randint(1, 6)
    print(sum)
print (sum)