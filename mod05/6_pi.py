import random

numberOfPoints = int(input("how many points"))

N = numberOfPoints
n = 0 # number of points inside circle

min = -1
max = 1

i = 0
while (i <= numberOfPoints):
    x = random.uniform(min, max)
    y = random.uniform(min, max)
    if (x**2+y**2 < 1):
        n += 1
    i += 1

print(f"{4*n/N}")

# pi = math.pi
# A = pi/4