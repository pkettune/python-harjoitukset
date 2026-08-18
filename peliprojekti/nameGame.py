import random

name = input("WHAT IS YOUR NAME?\n")
age = int(input("WHAT IS YOUR AGE?\n"))
komento = str

while(input):
    if(age < 12):
        print("alaikäinen")
        break
    if(age >= 12):
        print("\nwelcome " + name+"\n")

    while(komento != "lopeta"):
        print("Komennot:\n'a'\n'dice'\n'c'\n'lopeta'\n")
        komento = input("Anna komento: ")
        if komento == "a":
            print("a")
            break
        if komento == "dice":
            print(f"\nDice rolled: {random.randint(1, 6)}")
            break
        if komento == "c":
            print("c")
            break
    

#print (f"Player name: {name}\nPlayer age: {age}")

