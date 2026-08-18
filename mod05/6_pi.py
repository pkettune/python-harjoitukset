import random
import math

numberOfPoints = int(input("how many points"))
i = 0
n = 0

min = -1
max = 1

x = random.uniform(min, max)
y = random.uniform(min, max)

while (i <= numberOfPoints):
    if (x**2+y**2 < 1):
        print(x, y)
        n = n + 1
    else:
        n = n
    i = i + 1


