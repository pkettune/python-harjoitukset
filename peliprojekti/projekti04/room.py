import item
import random

roomList = {}
foundItem = None

class Room:
    def __init__(self, xCor, yCor):
        itemToFind = object
        self.roomNumber = xCor, yCor
        spawnNumber = random.randint(1, 10)
        print (spawnNumber)
        if (spawnNumber == 1):
            itemToFind = item.Knife()
            roomList[self.roomNumber] = itemToFind
        elif (spawnNumber == 2):
            itemToFind = item.Rock()
            roomList[self.roomNumber] = itemToFind
        elif (spawnNumber == 3):
            itemToFind = item.Note()
            roomList[self.roomNumber] = itemToFind
        else:
            itemToFind = None
        #roomList[self.roomNumber] = itemToFind
        self.foundItem = itemToFind
        print(f"{itemToFind}")

r = Room(0, 0)

#print(f"{roomList[itemToFind]}")