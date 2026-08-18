import random

name = input("WHAT IS YOUR NAME?\n")
age = int(input("WHAT IS YOUR AGE?\n"))
komento = str

while(komento != "lopeta"):
    if(age < 12):
        print("alaikäinen")
        break
    if(age >= 12):
        print("\nwelcome " + name)

        while (input):
            print("\nKomennot:\n'a'\n'dice'\n'time'\n'lopeta'\n")
            komento = input("Anna komento: ")
            if komento == "a":
                print("\na is the first letter of the alphabet")
            elif komento == "dice":
                print(f"\nDice rolled: {random.randint(1, 6)}")
            elif komento == "time":
                print("\nit's showtime")
            elif (komento == "lopeta"):
                break
            else:
                print("\nWRONG INPUT!")