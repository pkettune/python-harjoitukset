import random

number = random.randint(1,10)

while (number):
    guess = int(input("Guess the number\n"))
    if (guess < number):
        print("Liian pieni arvaus")
    elif (guess > number):
        print("Liian suuri arvaus")
    else:
        print("Oikein")
        break