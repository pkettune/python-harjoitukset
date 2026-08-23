import random
import player

name = input("WHAT IS YOUR NAME?\n")
age = int(input("WHAT IS YOUR AGE?\n"))
komento = str

itemList = []

def add_item():
    item = input("What item you want to add? ")
    itemList.append(item)
    return

def show_items():
    #for i in itemList:
    print(itemList)
    return

def change_name():
    newName = input("Tell me your new name\n")
    name = newName
    print("\nWelcome " + name)
    return


while(komento != "lopeta"):
    if(age < 12):
        print("alaikäinen")
        break
    if(age >= 12):
        print("\nWelcome " + name)

        while (input):
            print("\nKomennot:\n'a(add item)'\n's(show items)'\n'name(change name)'\n'lopeta'\n")
            komento = input("Anna komento: ")
            if komento == "a":
                add_item()
                #print("\na is the first letter of the alphabet")
            elif komento == "s":
                show_items()
                #print(f"\nDice rolled: {random.randint(1, 6)}")
            elif komento == "name":
                change_name()
                #print("\nit's showtime")
            elif (komento == "lopeta"):
                break
            else:
                print("\nWRONG INPUT!")