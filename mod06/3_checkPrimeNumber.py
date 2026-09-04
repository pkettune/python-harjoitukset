numberInput = int(input("Check if number is a prime number\n"))

numbers = list(range(numberInput))
## TAI NÄIN
# for i in range(numberInput):
#     numbers.append(i)

primeNumber = bool()

#aloitetaan indexistä 2, koska emme halua jakaa 0:lla tai 1:llä
for n in range(2, numberInput):
    if numberInput % numbers[n] == 0:
        primeNumber = False
        print("Not a prime number")
        break
    elif numberInput % numbers[n] != 0:
        primeNumber = True

if primeNumber == True:
    print("It's a prime number!")