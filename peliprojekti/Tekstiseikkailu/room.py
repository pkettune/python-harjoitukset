from items import Item
import random

roomList = {}

class Room:
    def __init__(self, name, itemToFind):
        self.name = name
        self.itemToFind = itemToFind
        roomList[name] = itemToFind
        return roomList






# class Room:
#     def __init__(self, xCor, yCor):
#         itemToFind = object
#         self.roomNumber = xCor, yCor
#         spawnNumber = random.randint(1, 10)
#         print (spawnNumber)
#         if (spawnNumber == 1):
#             itemToFind = Item("Knife")
#             roomList[self.roomNumber] = itemToFind
#         elif (spawnNumber == 2):
#             itemToFind = Item("Rock")
#             roomList[self.roomNumber] = itemToFind
#         elif (spawnNumber == 3):
#             itemToFind = Item("Note")
#             roomList[self.roomNumber] = itemToFind
#         else:
#             itemToFind = None
#         #roomList[self.roomNumber] = itemToFind
#         print(f"{itemToFind}")

# r = Room(0, 0)

#print(f"{roomList[itemToFind]}")