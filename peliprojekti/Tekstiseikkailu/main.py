import random
from player import Player
from room import Room
from items import Item
from tools import clear_screen

name = input("WHAT IS YOUR NAME?\n")
age = int(input("WHAT IS YOUR AGE?\n"))
komento = str

itemList = []


while(komento != "lopeta"):
    if(age < 12):
        print("alaikäinen")
        break
    if(age >= 12):
        print("\nWelcome " + name)
        Player(name)
        clear_screen
        while (input):
            print("\nKomennot:\n'a(add item)'\n's(show items)'\n'name(change name)'\n'lopeta'\n")
            komento = input("Anna komento: ")
            if komento == "a":
                Player.collect_item(Room.itemToFind)
                #print("\na is the first letter of the alphabet")
            elif komento == "s":
                Item.show_items(name, itemList)
                #print(f"\nDice rolled: {random.randint(1, 6)}")
            elif komento == "name":
                Player.change_name()
                #print("\nit's showtime")
            elif (komento == "lopeta"):
                break
            else:
                print("\nWRONG INPUT!")