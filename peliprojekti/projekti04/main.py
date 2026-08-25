import random
from player import Player
from room import Room
from items import Item

name = input("WHAT IS YOUR NAME?\n")
age = int(input("WHAT IS YOUR AGE?\n"))
komento = str

itemList = []
#sadf
def add_item(item):
    Player.collect_item(item)
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
        Player(name, itemList, 0, 0)

        while (input):
            print("\nKomennot:\n'a(add item)'\n's(show items)'\n'name(change name)'\n'lopeta'\n")
            komento = input("Anna komento: ")
            if komento == "a":
                add_item(Room.itemToFind)
                #print("\na is the first letter of the alphabet")
            elif komento == "s":
                Player.show_items()
                #print(f"\nDice rolled: {random.randint(1, 6)}")
            elif komento == "name":
                change_name()
                #print("\nit's showtime")
            elif (komento == "lopeta"):
                break
            else:
                print("\nWRONG INPUT!")