<<<<<<< HEAD:peliprojekti/room.py
from items import Item
=======
import peliprojekti.projekti04.item as item
>>>>>>> 0a4762588685130a1b76dbf14766f40617105648:peliprojekti/projekti04/room.py
import random

roomList = {}

class Room:
    def __init__(self, xCor, yCor):
        itemToFind = object
        self.roomNumber = xCor, yCor
        spawnNumber = random.randint(1, 10)
        print (spawnNumber)
        if (spawnNumber == 1):
            itemToFind = Item("Knife")
            roomList[self.roomNumber] = itemToFind
        elif (spawnNumber == 2):
            itemToFind = Item("Rock")
            roomList[self.roomNumber] = itemToFind
        elif (spawnNumber == 3):
            itemToFind = Item("Note")
            roomList[self.roomNumber] = itemToFind
        else:
            itemToFind = None
        #roomList[self.roomNumber] = itemToFind
        print(f"{itemToFind}")

r = Room(0, 0)

#print(f"{roomList[itemToFind]}")